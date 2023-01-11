from pwn import *
from Crypto.Util.number import *

server = process("./server.py")
# server = remote("127.0.0.1", 1337)

k = 64
l = 8

"""
	Retrieve the parameters
"""
server.recvuntil(b"a = ")
a = int(server.recvline().decode().strip())
server.recvuntil(b"b = ")
b = int(server.recvline().decode().strip())
m = 2**(2*k)
"""
	Get and store the outputs
"""
out = [int(server.recvline().decode().strip()) for _ in range(2023)]

"""
	
"""
def solve_LCG(a, m, approx):

	n = len(approx)
	M = Matrix(ZZ, n, n)
	for i in range(1, n):
		M[i, i] = -1
		M[i, 0] = a**i
	M[0, 0] = m
	
	L = M.LLL()

	v = vector([x for x in approx])
	lower_bits = L.solve_right(vector([round(RR(x)/m) * m - x for x in L * v]))

	return list(v + lower_bits)

"""
	
"""
mm = 2**(k + l)
mmm = 2**k
for period in range(k+1, 2038 // 16):

	if isPrime(period):
		continue

	A = pow(a, period, mm)
	for guess in range(2**l):
		LSB = [int(pow(A, i, 2**l)) * guess % 2**l for i in range(16)]
		MSB = [(LSB[i] ^^ (out[i * period] % 2**l)) << k for i in range(16)]
		recover = solve_LCG(A, mm, MSB)
	
		right = int(recover[0])
		right %= mmm
		left = out[0] ^^ right
		_seed = int(pow(a, -1, m)) * ((left << k) + right) % m
	
		check = True
		state = _seed
		for i in range(2023):
			state = a * state % m
			
			if bin((state >> k) ^^ (state % mmm)).count("1") % 2 != bin(out[i]).count("1") % 2:
				check = False
				break

		if check:
			server.sendlineafter(b"Guess the seed: ", str(_seed).encode())
			print(server.recvline().decode())
			exit()				

	print(period)
