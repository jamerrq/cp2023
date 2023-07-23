import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):

    n = read()
    M = read_array()

    #
    M.sort()
    lvl = 1
    ans = M[0] - lvl
    for mi in M[1:]:

        if mi - lvl > 1:
            lvl += 1
            ans += mi - lvl

        else:
            lvl = max(mi, lvl)

    print(ans)
