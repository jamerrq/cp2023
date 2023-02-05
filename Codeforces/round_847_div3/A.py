import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


pi = '3141592653589793238462643383279'
t = read()

for _ in range(t):
    n = read(str)
    ans = 0
    for i in range(len(n)):
        if n[i] == pi[i]:
            ans += 1
        else:
            break

    print(ans)
