import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()

for _ in range(t):
    n = read()
    s = read(str)
    x = 0
    y = 0

    ans = 'no'

    for c in s:

        if c == 'L':
            x -= 1
        if c == 'R':
            x += 1
        if c == 'U':
            y += 1
        if c == 'D':
            y -= 1
        
        if x == 1 and x == y:
            ans = 'yes'
            break

    print(ans)
