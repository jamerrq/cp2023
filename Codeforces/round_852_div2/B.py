import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    x, y = read_array()
    #
    n = 2 * (x - y)
    A = [0] * n
    #
    idx = 0
    for i in range(y, x + 1):
        A[idx] = i
        idx += 1
    for i in range(x - 1, y, -1):
        A[idx] = i
        idx += 1

    print(n)
    print(' '.join([str(ai) for ai in A]))
