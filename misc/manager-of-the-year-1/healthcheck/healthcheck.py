#!/usr/bin/env python3

import numpy as np
from pwn import remote, context

n_days = 365
preds = np.zeros(n_days)
sol = []
debug = False

def recvline(proc):
    line = proc.recvline()
    if debug:
        print(line)
    if b'Well done' in line and b'idek{' in line:
        print(line)
        exit(0)
    return line

def oracle(proc, preds):
    preds = ' '.join(str(a) for a in preds).encode()
    proc.sendline(preds)

    line = recvline(proc)

    rmse = float(line.split(b'RMSE (')[1].split(b')')[0])

    proc.recvuntil(b'(in thousands) for 2023:\n')

    return rmse

proc = remote('127.0.0.1', 1337)

for _ in range(2):
    recvline(proc)

proc.sendline(b'')
proc.recvuntil(b'(in thousands) for 2023:\n')

baseline_rmse = oracle(proc, preds)

for i in range(n_days):
    preds[i] = 1

    rmse = oracle(proc, preds)
    sol.append((n_days * (baseline_rmse ** 2 - rmse ** 2) + 1)/2)

    preds[i] = 0

oracle(proc, sol)
exit(1)