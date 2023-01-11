# Challenge Name: Gone Fishing
**Category:** Rev
**Difficulty:** Easy/Medium
**Author:** Kaligula

## Description
Fishing is a great hobby; if you look around very very carefully you are bound to get hooked!
Author's note: This is a boot2root challenge with a rev twist
Infra's note: There is a 10 minute timeout once PoW is solved.

## Flag
idek{wh4l3_WhA1e_wH4le_15_7h15_a_5h3l1}



## Notes
This VM has an installed LKM rootkit with 2 main functions: 
1. Hooking syscalls
2. Hiding itself 
The rootkit has a backdoor built into it which will give the user root if all the hooks are put in place. It can be discovered by running lsmod.
1. symlink syscall hook: checks that the file path is /etc/passwd, and the link path is /tmp/fishing. This sets up the prng hook
2. prng hook (_get_random_bytes.part.0): Basically messes up prng so that all random numbers generated are 0. 
3. rename syscall hook: checks that the old file name xored with 3 is equal to "somethingfishy". Enables the kill hook
4. kill syscall hook: Checks that 2 randomly generated numbers are equal to each other, and if so, gives the user root

## Distribution
No files are provided to the players for this chall
