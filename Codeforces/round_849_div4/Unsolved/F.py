import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def sum_digits(x, k=0):
    if not k:
        return x
    
    sx = sum([int(xi) for xi in str(x)])
    return sum_digits(sx, k - 1)


t = read()
for _ in range(t):
    n, q = read_array()
    A = read_array()
    lvls = [0] * n
    for _ in range(q):
        query = read_array()
        opt = int(query[0])

        if opt - 1:
            x = int(query[1])
            nx = sum_digits(A[x - 1], lvls[x - 1])
            print(nx)
        else:
            lf, rg = int(query[1]), int(query[2])
            for i in range(lf - 1, rg):
                lvls[i] += 1
