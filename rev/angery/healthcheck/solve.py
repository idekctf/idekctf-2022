from pwn import *
import angr
import claripy
import base64

def solve():
    FLAG_LEN = 60
    STDIN_FD = 0

    base_addr = 0x4010B0

    elf = ELF('/tmp/challenge')

    proj = angr.Project("/tmp/challenge", main_opts={'base_addr': base_addr})

    flag_chars = [claripy.BVS('flag_%d' % i, 8) for i in range(FLAG_LEN)]
    flag = claripy.Concat( *flag_chars + [claripy.BVV(b'\n')])

    state = proj.factory.full_init_state(
            args=['challenge'],
            add_options=angr.options.unicorn,
            stdin=flag,
    )

    # Add constraints that all characters are printable
    for k in flag_chars:
        state.solver.add(k >= ord('!'))
        state.solver.add(k <= ord('~'))

    simgr = proj.factory.simulation_manager(state)
    find_addr  = elf.symbols['lose'] # SUCCESS
    avoid_addr = elf.symbols['win'] # FAILURE
    simgr.explore(find=find_addr, avoid=avoid_addr)

    

    if (len(simgr.found) > 0):
        for found in simgr.found:
            print("FOUND", found.posix.dumps(STDIN_FD).decode())

con = remote('127.0.0.1', 1337)

con.sendlineafter(b'[*] Press enter when you\'re ready!', b'')

data = con.recvline().strip()

data = base64.b64decode(data)

if data.startswith('\x7fELF'):
    exit(0)
exit(1)

# # print(data)


# f = open('/tmp/challenge', 'wb')
# f.write(data)
# f.close()


# solve()

