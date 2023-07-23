import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


# helped by the tutorial [https://codeforces.com/blog/entry/111948]
t = read()
for _ in range(t):

    n = read()

    f = []
    m = [[0] * (n - 1) for _ in range(n)]
    for i in range(n):
        m[i] = read_array()
        f.append(m[i][0])

    f.sort()
    f1, f2 = f[0], f[-1]
    if f1 != f[1]:
        f1, f2 = f2, f1

    for mi in m:
        if mi[0] == f2:
            print(f1, ' '.join([str(x) for x in mi]))
            break
