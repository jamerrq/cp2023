import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n, c = read_array()
    A    = read_array()

    for i in range(n):
        A[i] += i + 1
    
    A.sort()

    ans = 0
    i = 0
    while i < n:
        if A[i] <= c:
            c -= A[i]
            ans += 1
        else:
            break

        i += 1
    
    print(ans)
