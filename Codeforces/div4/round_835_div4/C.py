import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n = read()
    S = read_array()
    C = sorted(S.copy())
    #
    m1, m2 = C[-1], C[-2]
    for i in range(n):
        if m1 - S[i]:
            C[i] = S[i] - m1
        else:
            C[i] = m1 - m2

    print(' '.join([str(x) for x in C]))
