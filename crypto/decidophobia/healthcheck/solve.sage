from pwn import *

server = process("./server.py")
# server = remote("127.0.0.1", 1337)

"""
	Get RSA-encrypted ticket `enc` and the modulus `n`
"""
server.sendlineafter(">>>", "1")
server.recvuntil("n = ")
n = int(server.recvline().decode().strip())
server.recvuntil("enc = ")
enc = int(server.recvline().decode().strip())

"""
	Get information provided by RSA-based OT, notice that we don't need to know `x3` 
"""
server.sendlineafter(">>>", "2")
server.sendlineafter(">>>", "2") # Ignore Mercury for sure
server.recvuntil("N = ")
N = int(server.recvline().decode().strip())
server.recvuntil("x1 = ")
x1 = int(server.recvline().decode().strip())
server.recvuntil("x2 = ")
x2 = int(server.recvline().decode().strip())

"""
	Compute the cool value `v` so that the linear combination `hint` of p and q can be revealed
"""
nbits, mbits = 512, 384
k = 2 * mbits - nbits
a = -2**k
ae = int(pow(a, 0x10001, N))
v = (ae * x2 - x1) * inverse_mod(ae - 1, N) % N

server.sendlineafter("Gimme your response: ", str(int(v)))
server.recvuntil("c1 = ")
c1 = int(server.recvline().decode().strip())
server.recvuntil("c2 = ")
c2 = int(server.recvline().decode().strip())

"""
	Calculate the coefficients, which will be used later
		`q_h`: higher bits of q
		`p_l`: lower bits of p
		`s`  : the sum of lower bits of q and higher bits of p
"""
hint = (c1 - a * c2) % N
q_h = hint >> nbits
p_l = hint % 2**k
s = (hint >> k) % 2**(nbits-k)

"""
	Construct the polynomial and run Coopersmith with suitable parameters
"""
PR.<x> = PolynomialRing(Zmod(n))
f = (q_h * 2**(nbits-k) + (s-x)) * (x * 2**k + p_l)
f = f.monic()
x = f.small_roots(X = 2^(nbits-k), beta = 0.6, epsilon = 0.36 - (nbits-k)/(3*nbits-1))
for xx in x:
	p = int(xx) * 2**k + p_l
	if n % p == 0:
		q = (hint - p) // 2**k
		r = n // p // q
		d = int(pow(0x10001, -1, (p-1)*(q-1)*(r-1)))
		ticket = pow(enc, d, n)

		server.sendlineafter(">>>", "4")
		server.sendlineafter("Give me your ticket. ", str(int(ticket)))
		_ = server.recvline() 
		flag = server.recvline()
		print(flag)
		exit(0)
exit(1)
		
