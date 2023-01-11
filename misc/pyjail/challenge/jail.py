#!/usr/bin/env python3

blocklist = ['.', '\\', '[', ']', '{', '}',':']
DISABLE_FUNCTIONS = ["getattr", "eval", "exec", "breakpoint", "lambda", "help"]
DISABLE_FUNCTIONS = {func: None for func in DISABLE_FUNCTIONS}

print('welcome!')

while True:
    cmd = input('>>> ')
    if any([b in cmd for b in blocklist]):
        print('bad!')
    else:
        try:
            print(eval(cmd, DISABLE_FUNCTIONS))
        except Exception as e:
            print(e)
