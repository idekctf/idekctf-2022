#!/usr/bin/env python3

def main():
    blocklist = ['.', '\\', '[', ']', '{', '}',':', "blocklist", "globals", "compile"]
    DISABLE_FUNCTIONS = ["getattr", "eval", "exec", "breakpoint", "lambda", "help"]
    DISABLE_FUNCTIONS = {func: None for func in DISABLE_FUNCTIONS}

    print('welcome!')

    # NO LOOP!

    cmd = input('>>> ')
    if any([b in cmd for b in blocklist]):
        print('bad!')
    else:
        try:
            print(eval(cmd, DISABLE_FUNCTIONS))
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()