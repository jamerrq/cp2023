import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n = read()
    s = read(str)
    i = 0
    j = n - 1

    while i < j:
        ci = s[i]
        cj = s[j]
        if ci != cj:
            i += 1
            j -= 1
        else:
            break

    if i == j:
        print(1)
    elif i < j:
        print(j - i + 1)
    else:
        print(0)
