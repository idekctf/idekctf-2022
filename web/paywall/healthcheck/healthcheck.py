#!/usr/bin/env python3

import requests

s = requests.session()

if s.get("http://127.0.0.1/articles/flag").status_code != 403: exit(1)
if s.get("http://127.0.0.1/").status_code != 200: exit(1)
if s.get("http://127.0.0.1/?p=checker").status_code != 200: exit(1)

exit(0)
