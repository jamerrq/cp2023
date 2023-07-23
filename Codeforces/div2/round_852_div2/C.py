import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n = read()
    A = read_array()
    #
    mx, mn = n, 1
    l = 0
    r = n - 1
    while l <= r:

        if A[l] == mx:
            l += 1
            mx -= 1
        elif A[l] == mn:
            l += 1
            mn += 1
        elif A[r] == mx:
            r -= 1
            mx -= 1
        elif A[r] == mn:
            r -= 1
            mn += 1
        else:
            break

    if l <= r:
        print(l + 1, r + 1)
    else:
        print(-1)
