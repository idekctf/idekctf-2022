from random import randint

from malbolge import malbolge

crazy = [[randint(0, 2) for _ in range(3)] for _ in range(3)]
assert crazy != [[1, 0, 0], [1, 0, 2], [2, 2, 1]]  # no cheese for you
print(crazy)
exec(malbolge(input(), stdin_allowed=False, a_bad_time=crazy))
