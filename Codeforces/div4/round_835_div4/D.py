import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n = read()
    A = read_array()
    V = [0] * n
    for i in range(n):
        if i == 0:
            V[i] = 1
        elif i < n - 1:
            if A[i] == A[i - 1]:
                # print(i)
                if V[i - 1]:
                    V[i - 1] = 0
                    V[i] = 1
                    # print(i)
            elif A[i] < A[i - 1]:
                if V[i - 1]:
                    V[i - 1] = 0

                V[i] = 1
        else:
            if A[i] == A[i - 1] and V[i - 1]:
                V[i - 1] = 0
                V[i] = 1
            elif A[i] < A[i - 1]:
                if V[i - 1]:
                    V[i - 1] = 0

                V[i] = 1

    # print(V)
    if sum(V) == 1:
        print('YES')
    else:
        print('NO')
