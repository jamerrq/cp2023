import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):

    n = read()
    a, b = 0, 0
    inA = False
    a += min(1, n)
    n -= a
    cnt = 2

    while n:

        ad = min(cnt * 2 + 1, n)

        if not inA:
            n -= ad
        else:
            a += ad

        inA = not inA
        cnt += 2
        n -= ad

    print(a, b)
