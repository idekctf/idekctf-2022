with open('out.txt', 'r') as file:
    x = bytes.fromhex(file.read())

x = [*map(ZZ, x)]
p = 127
E = GF(p^32, 't')
π = E.frobenius_endomorphism()

for i in range(0, len(x), 32):
    c = E([ZZ(y) for y in x[i:i+32]])

    for f in π.powers(E.degree()):
        m = f(c).polynomial()
        if m.degree() < 16:
            print(*map(chr, m.list()), sep='')