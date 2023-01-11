#!/usr/bin/env python3

from pwn import *

# server = process("./server.py")
server = remote("127.0.0.1", 1337)

"""
	Check the banner
"""
server.recvuntil(b"Here is your random token: ")
server.recvuntil(b"times exponentiation to get the valid ticket")

"""
	Check whether the entire menu is sent
"""
server.recvuntil(b"[1] Broken Oracle")
server.recvuntil(b"[2] Verify")
server.recvuntil(b"[3] Exit")

"""
	Check the first option
"""
server.sendlineafter(b">>>", b"1")
server.sendlineafter(b"Tell me the token. ", b"0")
server.sendlineafter(b"What is your calculation? ", b"0")
server.recvuntil(b"Your are correct!")
server.sendlineafter(b">>>", b"1")
server.sendlineafter(b"Tell me the token. ", b"0")
server.sendlineafter(b"What is your calculation? ", b"1")
server.recvuntil(b"Nope, the ans is 0...")

"""
	Check the second option
"""
server.sendlineafter(b">>>", b"2")
server.sendlineafter(b"Give me the ticket. ", b"0")
server.recvuntil(b"Nope :<")

"""
	Check the exit command
"""
server.sendlineafter(b">>>", b"3")
