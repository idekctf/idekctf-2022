#!/usr/bin/env python3

import requests

resp = requests.post("http://127.0.0.1:1337/just-read-it", json={"orders":[100,100,100,99,99,99,40]})

if b"idek{" in resp.content:
    exit(0)

exit(1)