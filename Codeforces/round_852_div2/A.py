import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    a, b = read_array()
    n, m = read_array()

    ans = 0

    while n:

        if n > m:
            vx = n // (m + 1)
            p1 = a * m * vx
            p2 = b * (m + 1) * vx
            #
            ans += min(p1, p2)
            n -= (m + 1) * vx
        else:
            p1 = a * n
            p2 = b * n
            #
            ans += min(p1, p2)
            n = 0

    print(ans)
