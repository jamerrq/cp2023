import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):

    n = read()
    A = read_array()
    l = [0] * n
    r = [0] * n
    #
    l[0] = A[0]
    r[-1] = A[-1]
    #
    for i in range(n - 1):
        l[i + 1] = l[i] * A[i + 1]
        r[-i-2] = r[-i-1] * A[-i-2]

    ans = -1
    for i in range(n - 2, -1, -1):
        if l[i] == r[i + 1]:
            ans = i + 1

    # print(l, r, ans)
    print(ans)
