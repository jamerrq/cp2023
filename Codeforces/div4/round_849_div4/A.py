import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    a = read(str)
    if a in "codeforces":
        print('yes')
    else:
        print('no')
