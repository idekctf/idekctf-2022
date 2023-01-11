#!/usr/bin/env python3

from pwn import *

context.log_level = 'debug'

# server = process("./server.py")
server = remote("127.0.0.1", 1337)

"""
	Check the welcome message
"""
server.recvuntil(b"I'll give you 2023 consecutive outputs of the RNG,")
server.recvuntil(b"you just need to recover the seed. Sounds easy, right?")

"""
	Check whether the parameters are sent
"""
server.recvuntil(b"a = ")
server.recvuntil(b"b = ")
server.recvline()

"""
	Check the outputs
"""
for _ in range(2023):
	r = server.recvline()
print("REEE")
server.sendlineafter(b"Guess the seed: ", b"0")
server.recvuntil(b"Nope :<")
