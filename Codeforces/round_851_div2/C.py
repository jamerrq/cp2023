import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def sum_digits(n):
    return sum([int(x) for x in str(n)])


t = read()
for _ in range(t):
    n = read()
    if n % 2:
        print('Yes')
        m = (n - 1) // 2
        for i in range(1, n + 1):
            if i < m + 1:
                print(i, 3 * m + 3 + i - 1)
            else:
                print(i, 2 * m + 2 + i - m - 1)
    else:
        print('No')
        continue
