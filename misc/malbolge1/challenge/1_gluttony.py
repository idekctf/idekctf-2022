from malbolge import malbolge

assert len(code := input()) <= 66 - 6 + (6 + 6)/6
exec(malbolge(code))
