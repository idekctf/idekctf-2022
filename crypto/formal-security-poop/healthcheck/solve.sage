from Crypto.Util.Padding import pad
from Crypto.Util.number import sieve_base
from Crypto.Cipher import AES
from ecc import sha512,  Point, p,  E as E_, G as G_

from pwn import process, remote, context
#context.log_level = 'debug'

def option(opt):
    io.sendlineafter(b'>>> ', str(opt).encode())

def read_point(E):
    io.recvuntil(b'x = ')
    x = int(io.recvline(False))
    io.recvuntil(b'y = ')
    y = int(io.recvline(False))
    return E(x, y)

def send_point(P):
    io.sendlineafter(b'x = ', str(P[0]).encode())
    io.sendlineafter(b'y = ', str(P[1]).encode())

def session(X):
    send_point(X)
    B = read_point(E)
    Y = read_point(E)
    return B, Y

def sign():
    option(3)
    io.sendlineafter(b'? ', b'AZ')
    io.recvuntil(b'r = ')
    r = int(io.recvline(False))
    io.recvuntil(b's = ')
    s = int(io.recvline(False))
    return r, s


def H(P) -> int:
    z = int(P[0]).to_bytes(32, 'big') + int(P[1]).to_bytes(32, 'big')
    return int.from_bytes(sha512(z).digest(), 'big') % p

def cipher(b):
    S = (y + H(Y)*b)*X
    key = sha512(H(S).to_bytes(32, 'big')).digest()[:16]
    return AES.new(key, AES.MODE_ECB)

def low_order_points():
    last_coeff = 7

    while 1:
        print('.', end='')
        last_coeff += 1
        R = EllipticCurve(GF(p), [E_.a, last_coeff]).random_point()
        o = R.order()

        for (q, v) in factor(o):
            m = q^v
            if m > 2^16 or m in moduli:
                continue

            print(f'\nm = {q}^{v}')
            X = (o//m)*R
            assert m == X.order()
            yield m, X

def recover_ephemeral_key():
    m = int.from_bytes(sha512(b'key verification').digest(), 'big') % p
    n = 3
    sigs = [sign() for _ in range(n)]

    M = matrix([
        [-m]*n,
        [-r for r, _ in sigs],
    ]).stack(
        matrix.diagonal([s for _, s in sigs])
    ).stack(
        matrix.identity(n)*p
    ).augment(
        matrix.identity(n + 2)
        .stack(matrix(n, n + 2))
    ).dense_matrix()

    print('='*100)
    print(*M, sep='\n')
    print('='*100)

    W = matrix.diagonal([p^2]*n + [1, 1/p] + [1/2^32]*n)

    for row in (M*W).LLL()/W:
        if row[:n] == 0 and abs(row[n]) == 1:
            y = row[n]*row[n+1] % p
            return int(y)

    print("[!] Couldn't recover y!")

#io = remote('127.0.0.1', 1337)
io = process(['python3', './main.py'])

E = EllipticCurve(GF(p), [E_.a, E_.b])
G = E(G_.x, G_.y)

# Setup checkup string
send_point((0, 0))
B, Y = session(G)
S = Y + H(Y)*B

key = sha512(H(S).to_bytes(32, 'big')).digest()[:16]
aes = AES.new(key, AES.MODE_ECB)
pt = pad(b'key verification', 16)

option(1)
io.sendlineafter(b'? ', b'AZ')
io.sendlineafter(b'= ', aes.encrypt(pt).hex())
print(io.recvline(False).decode())


remain = []
moduli = []

for m, X in low_order_points():
    option(4)
    B, Y = session(X)

    while gcd(H(Y), m) != 1:
        print("Unfavorable H(Y), resetting session")
        option(4)
        B, Y = session(X)

    y = recover_ephemeral_key()
    print('y =', y)

    # Retrieve checkup string
    option(2)
    io.sendlineafter(b'? ', b'AZ')
    send_point(G)
    io.sendlineafter(b's = ', b'1')

    io.recvuntil(b'secret = ')
    ct = bytes.fromhex(io.recvline(False).decode())

    for r in range(m):
        if cipher(r).decrypt(ct) == pt:
            print(f'b mod {m} =', r)
            remain.append(r)
            moduli.append(m)
            break
    else:
        print("[!] Couldn't find b!")

    if lcm(moduli).nbits() > p.bit_length():
        break

print('r =', remain)
print('m =', moduli)
print('b =', b := CRT(remain, moduli))
assert b*G == B

option(2)
io.sendlineafter(b'? ', b'Bob')
send_point((0, 0))
io.recvuntil(b'c = ')
c = int(io.recvline(False))
io.sendlineafter(b's = ', str(c*b).encode())

print('-'*100)
io.recvuntil(b'secret = ')
ct = bytes.fromhex(io.recvline(False).decode())
print(cipher(b).decrypt(ct))
