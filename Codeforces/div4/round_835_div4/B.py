import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()

for _ in range(t):
    n = read()
    s = read(str)
    #
    ans = 0
    for char in s:
        ans = max(ord(char) - 96, ans)

    print(ans)
