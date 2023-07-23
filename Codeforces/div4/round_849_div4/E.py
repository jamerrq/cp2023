import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n = read()
    A = read_array()
    negs = 0

    for i in range(n):
        if A[i] < 0:
            negs += 1
            A[i] = -A[i]
    
    A.sort()

    if negs % 2:
        A[0] = -A[0]

    # for i in range(n - 1):
    #     si = A[i] + A[i + 1]
    #     if -si > si:
    #         A[i] = -A[i]
    #         A[i + 1] = -A[i + 1]
    #     else:
    #         continue
    
    print(sum(A))
