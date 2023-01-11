from malbolge import malbolge

assert len(code := input()) < 66 + 6 + 6 + 666 // 6

BLACKLIST = ["breakpoint", "eval", "exec", "getattr", "help", "input", "lambda", "open"]
DISABLE_FUNCTIONS = {func: None for func in BLACKLIST}

exec(malbolge(code, stdin_allowed=False), DISABLE_FUNCTIONS)
