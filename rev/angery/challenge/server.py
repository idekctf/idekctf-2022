#!/usr/bin/env python3
import subprocess
import os
import base64
import time

print("[*] Hello, this is autorev challenge! You'll have 20 questions, each questions has 30 seconds to answer. If you defeat all my quiz, I'll give you my flag. Are you ready?", flush = True)

input("[*] Press enter when you're ready!")

for i in range(20):
    subprocess.run(["python3", "generate.py"])

    leak = open('/tmp/challenge', 'rb').read()
    print(base64.b64encode(leak).decode()+'\n', flush = True)
    print("[*] Your answer is: ", flush = True)

    start = time.time()
    result = subprocess.run(
        ["/tmp/challenge"], capture_output=True, text=True
    )
    delta = time.time() - start

    if delta > 30:
        print("[-] Times out!!", flush = True)
        exit(-1)

    if 'No!' in result.stdout:
        print("[-] Incorrect!! No flag for you...", flush = True)
        exit(-1)
    else:
        print("[+] Correct!!! Next challenge:", flush = True)

flag = open('./flag.txt', 'r').read()
print('Congratzzz!!! Here\'s your flag: {}'.format(flag), flush = True)