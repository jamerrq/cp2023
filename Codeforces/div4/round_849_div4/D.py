import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n = read()
    s = read(str)
    
    left_set, right_set = set(), set()
    left_sum, right_sum = [0] * n, [0] * n

    left_set.add(s[0])
    left_sum[0] = 1

    for i in range(1, n):
        ci = s[i]
        if ci in left_set:
            left_sum[i] = left_sum[i - 1]
        else:
            left_sum[i] = left_sum[i - 1] + 1
            left_set.add(ci)
    

    right_set.add(s[-1])
    right_sum[-1] = 1

    for i in range(n - 2, -1, -1):
        ci = s[i]
        if ci in right_set:
            right_sum[i] = right_sum[i + 1]
        else:
            right_sum[i] = right_sum[i + 1] + 1
            right_set.add(ci)
    
    ans = 0
    for i in range(n - 1):
        ans = max(ans, left_sum[i] + right_sum[i + 1])
    
    print(ans)
