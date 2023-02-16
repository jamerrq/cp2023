import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


k = read()
for _ in range(k):
    n, m = read_array()
    s = read(str)
    t = read(str)

    st = s + t[::-1]
    # print(st)
    ds = 0
    for i in range(1, n + m):
        if st[i] == st[i - 1]:
            ds += 1

    if ds < 2:
        print('YES')
    else:
        print('NO')
