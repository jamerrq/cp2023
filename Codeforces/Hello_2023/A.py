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
    ans = -1
    fnd = False
    #
    for i in range(n - 1):
        if s[i] == 'L' and s[i + 1] == 'R':
            ans = i
        if s[i] == 'R' and s[i + 1] == 'L':
            fnd = True

    if fnd:
        print(0)
    else:
        print(ans + int(ans != -1))
