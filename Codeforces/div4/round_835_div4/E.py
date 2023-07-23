import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):
    n = read()
    A = read_array()
    #
    ones = [0] * n
    fst0 = float('inf')
    ltr1 = -1
    ans = 0
    for i in range(n):
        ones[i] = A[i] + ones[i - 1]
        if A[i]:
            ltr1 = max(ltr1, i)
        else:
            fst0 = min(fst0, i)
            ans += ones[i - 1]

    # print(ans)
    # change first 0
    ansG = ans
    if fst0 < float('inf'):
        ones_left = ones[fst0]
        ones_right = ones[-1] - ones[fst0]
        nums_right = n - fst0 - 1
        zeros_right = nums_right - ones_right
        # print(ans + zeros_right - ones_left)
        ansG = max(ansG, ans + zeros_right - ones_left)

    if ltr1 != -1:
        ones_left = ones[ltr1] - 1
        ones_right = ones[-1] - ones[i]
        nums_right = n - ltr1 - 1
        zeros_right = nums_right - ones_right
        ansG = max(ansG, ans + ones_left - zeros_right)
        # print(ans + ones_left - zeros_right)

    print(ansG)
