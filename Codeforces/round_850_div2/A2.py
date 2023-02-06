import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):

    n = read()
    aw, bw, ab, bb = 0, 0, 0, 0
    inA = False
    aw += min(1, n)
    n -= aw
    cnt = 2

    while n:

        ad = min(cnt * 2 + 1, n)

        if not inA:
            bb += (ad + 1) // 2
            bw += ad // 2
        else:
            ab += ad // 2
            aw += (ad + 1) // 2

        inA = not inA
        cnt += 2
        n -= ad

    print(aw, ab, bw, bb)
