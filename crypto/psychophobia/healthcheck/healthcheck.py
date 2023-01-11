#!/usr/bin/env python3

import pwnlib.tubes

def handle_pow(r):
    print(r.recvuntil(b'python3 '))
    print(r.recvuntil(b' solve '))
    challenge = r.recvline().decode('ascii').strip()
    p = pwnlib.tubes.process.process(['kctf_bypass_pow', challenge])
    solution = p.readall().strip()
    r.sendline(solution)
    print(r.recvuntil(b'Correct\n'))

p = pwnlib.tubes.remote.remote('127.0.0.1', 1337)
print(p.recvuntil(b'== proof-of-work: '))
if p.recvline().startswith(b'enabled'):
    handle_pow(p)


p.recvuntil(b"Are you the psychic I requested")

exit(0)