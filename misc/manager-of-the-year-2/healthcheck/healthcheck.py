#!/usr/bin/env python3

from math import inf

import numpy as np
from pwn import remote

n_days = 365
preds = np.zeros(n_days)
debug = False

def recvline(proc):
    line = proc.recvline()
    if b'Well done' in line and b'idek{' in line:
        print(line)
        exit(0)
    if debug:
        print(line)
    return line

def oracle(proc, preds):
    preds = ' '.join(str(a) for a in preds).encode()
    proc.sendline(preds)

    line = recvline(proc)
    proc.recvuntil(b'(in thousands) for 2023:\n')
    
    if b'Are you sure' in line.strip():
        return True
    return False

proc = remote('127.0.0.1', 1337)

for _ in range(2):
    recvline(proc)

proc.sendline(b'')
#recvline(proc)

#for _ in range(n_days):
#    recvline(proc)

proc.recvuntil(b'(in thousands) for 2023:\n')
#proc.recvuntil(b'Data for 2023:\n')

#for _ in range(n_days):
#    recvline(proc)

#for _ in range(3):
#    recvline(proc)

for i in range(n_days):
    step = 50
    n_steps = 0
    n_steps_lim = 10
    sign = 1
    lim = 1e-3

    while n_steps < n_steps_lim:
        n_steps += 1
        preds[i] += sign * step

        if oracle(proc, preds):
            sign *= -1
        else:
            preds[i] += lim

            if oracle(proc, preds):
                sign = -1
            else:
                sign = 1

            preds[i] -= lim
        
        step /= 2

exit(1)