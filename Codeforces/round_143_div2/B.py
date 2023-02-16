import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n, k = read_array()
    mn, mx = float('inf'), -1
    #
    count = 0
    ints = []
    for _ in range(n):
        li, ri = read_array()
        if li <= k <= ri:
            count += 1
            mn = min(mn, li)
            mx = max(mx, ri)
            ints.append((li, ri))

    if count:
        dp = False
        for i in range(mn, mx + 1):
            if i == k:
                continue
            ct = 0
            for interval in ints:
                li, ri = interval
                if li <= i <= ri:
                    ct += 1

            if ct == count:
                dp = True

        if not dp:
            print('YES')
        else:
            print('NO')

    else:
        print('NO')