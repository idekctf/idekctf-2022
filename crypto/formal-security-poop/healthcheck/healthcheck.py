#!/usr/bin/env python3

from pwn import *

from pwn import remote

io = remote('127.0.0.1', 1337)
io.recvline(False)
assert b"What is your public key?" in io.recvline(False)

for _ in range(2):
    io.sendlineafter(b'x = ', b'-1')
    io.sendlineafter(b'y = ', b'-1')

io.sendlineafter(b'>>> ', b'-1')
assert b"My secrets are safe forever!" in io.recvline(False)
io.close()
exit(0)