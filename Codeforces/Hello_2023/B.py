import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n = read()
    if n % 2:
        if n < 5:
            print('NO')
        else:
            print('YES')
            k = (n - 1) // 2
            def ki(i):
                if i % 2:
                    return - k
                return k - 1
            print(' '.join([str(ki(i)) for i in range(n)]))
    else:
        print('YES')
        print(' '.join([str((-1) ** (i + 1)) for i in range(n)]))
