#!/usr/bin/env python3

import requests

s = requests.session()

if s.get("http://127.0.0.1:1337/").status_code != 200: exit(1)

exit(0)
