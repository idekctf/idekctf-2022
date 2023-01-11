#!/usr/bin/env python3

from pwn import *

# server = process("./server.py")
server = remote("127.0.0.1", 1337)

exit(1)