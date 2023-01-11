#!/usr/bin/env python3

from pwn import *
import random

server = process("./server.py")
# server = remote("127.0.0.1", 1337)

"""
	Get time-released crypto challenge 
"""
server.recvuntil(b"Here is your random token: ")
token = int(server.recvline().decode().strip())
server.recvuntil(b"The public modulus is: ")
n = int(server.recvline().decode().strip())
server.recvuntil(b"times exponentiation to get the valid ticket ")
_ = server.recvuntil(" % n!")
d = int(_.decode().split("2^(2^")[1].split("))")[0])

"""
	Query the oracle and setup the HNP
"""
DELTA = 0
def query(server, u):
	server.sendlineafter(b">>>", b"1")
	server.sendlineafter(b"Tell me the token. ", str(u).encode())
	server.sendlineafter(b"What is your calculation? ", b"0")
	server.recvuntil(b"Nope, the ans is ")
	_ = server.recvuntil(b"... (")
	MSB = int(_.decode().split("...")[0])
	_ = server.recvuntil(b"remain digits")
	lift = int(_.decode().split(" remain digits")[0])
	global DELTA
	DELTA = max(DELTA, 10**lift)
	return MSB * (10**lift)

m = 10
k = m * (m-1) // 2
u = [random.randint(2, n-1) for _ in range(m)]
A = [query(server, uu) for uu in u]
B = [query(server, uu * token) for uu in u]
M = Matrix(ZZ, k + 2*m + 1, k + 2*m + 1)
"""
        Inequality we derived by cross-multiplication
"""
idx = 0
for i in range(m):
	for j in range(i+1, m):
		M[i, idx] = B[j]
		M[j, idx] = -B[i]
		M[i+m, idx] = -A[j]
		M[j+m, idx] = A[i]
		M[2*m, idx] = A[i]*B[j] - A[j]*B[i]
		M[2*m+1+idx, idx] = n
		idx += 1	

"""
	Bound the value of xi and yi
"""
for i in range(2 * m):
	M[i, i+k] = DELTA
M[2*m, -1] = DELTA**2

M = M.LLL()
for i in range(k+2*m+1):
	if abs(M[i, -1]) == DELTA**2:
		print(f"FOUND! {i}")
		x = [abs(M[i, j] // DELTA) for j in range(k, k+m)]
		y = [abs(M[i, j] // DELTA) for j in range(k+m, k+2*m)]
		ans = (B[j] + y[j]) * inverse_mod(A[j] + x[j], n) % n
		break

"""
	Capture the flag!
"""
server.sendlineafter(b">>>", b"2")
server.sendlineafter(b"Give me the ticket. ", str(ans).encode())
server.interactive()
