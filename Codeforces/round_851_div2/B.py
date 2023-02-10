import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def sum_digits(n):
    return sum([int(x) for x in str(n)])


def solve(n):

    if n % 2:
        rem = n % 10
        if rem != 9:
            return (n + 1) // 2, (n - 1) // 2
        else:
            xp, yp = solve(n // 10)
            if sum_digits(xp) > sum_digits(yp):
                return 10 * xp + 4, 10 * yp + 5
            else:
                return 10 * xp + 5, 10 * yp + 4
    else:
        return n // 2, n // 2


t = read()
for _ in range(t):

    n = read()
    x, y = solve(n)
    print(x, y)
