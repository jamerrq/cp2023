import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n, c = read_array()
    A    = read_array()

    left = A.copy()
    for i in range(n):
        left[i] += i + 1
    
    right = A.copy()
    for i in range(n):
        right[i] += n - i
    
    used = [False] * n
    options = []
    for i in range(n):
        li = (left[i], i)
        ri = (right[i], i)
        
        options.extend([li, ri])

    ans = 0
    minR = right[0]
    indexMinR = 0
    for i in range(1, n):
        if right[i] < minR:
            indexMinR = i
            minR = right[i]
    
    if c <= minR:
        ans += 1
        c -= minR
        used[indexMinR] = True
    
    options.sort()
    i = 0
    while i < 2 * n:
        if not used[options[i][1]] and c <= options[i][0]:
            used[options[i][1]] = True
            ans += 1
            c -= options[i][0]
        
        i += 1
    
    print(ans)
