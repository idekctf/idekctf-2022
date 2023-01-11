#!/usr/bin/env python3

from pwn import *

# server = process("./server.py")
server = remote("127.0.0.1", 1337)

"""
	Check whether the entire menu is sent
"""
server.recvuntil(b"[1] Look in your backpack")
server.recvuntil(b"[2] Cry")
server.recvuntil(b"[3] Jump into the pool")
server.recvuntil(b"[4] Go to the party")
server.recvuntil(b"[5] Exit")

"""
	Check the first option
"""
server.sendlineafter(b">>>", b"1")
server.recvuntil(b"n = ")
server.recvuntil(b"enc = ")

"""
	Check the second option
"""
server.sendlineafter(b">>>", b"2")
server.recvuntil(b"[1] I lost my primes in the pool. It is the only thing I have, I cannot recover the key without it.")
server.recvuntil(b"[2] Ignore Mercury")
server.sendlineafter(b">>>", b"1")
server.recvuntil(b"N = ")
server.recvuntil(b"x1 = ")
server.recvuntil(b"x2 = ")
server.recvuntil(b"x3 = ")
server.sendlineafter(b"Gimme your response: ", b"0")
server.recvuntil(b"c1 = ")
server.recvuntil(b"c2 = ")
server.recvuntil(b"c3 = ")

server.sendlineafter(b">>>", b"2")
server.recvuntil(b"Mercury went back to the heaven ... ")

"""
	Check the third option
"""
server.sendlineafter(b">>>", b"3")
server.recvuntil(b"Find nothing ...")

"""
	Check the fourth option
"""
server.sendlineafter(b">>>", b"4")
server.sendlineafter(b"Guard: Give me your ticket. ", b"0")
server.recvuntil(b"Go away!")

"""
	Check the exit command
"""
server.sendlineafter(b">>>", b"5")
