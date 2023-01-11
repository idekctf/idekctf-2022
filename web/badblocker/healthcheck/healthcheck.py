#!/usr/bin/env python3

import requests

s = requests.session()

urls = [
	"http://127.0.0.1:1337/",
	"http://127.0.0.1:1337/http://www.example.org",
	"http://127.0.0.1:1337/blocked.html"
]

for url in urls:
	if s.get(url).status_code != 200: exit(1)

exit(0)