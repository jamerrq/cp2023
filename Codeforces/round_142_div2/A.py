import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def binary_search(arr, x):
    #
    i, j = 0, len(arr) - 1
    ans = -1
    #
    while i <= j:

        mid = i + (j - i) // 2
        xmd = arr[mid]

        if xmd <= x:
            ans = mid
            i = mid + 1

        else:
            j = mid - 1

    return ans


def gcd(a, b):
    """
    https://cp-algorithms.com/algebra/euclid-algorithm.html
    """
    if not b:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    return a / gcd(a, b) * b



t = read()
for _ in range(t):
    n = read()
    H = read_array()
    #
    o = sum([int(hi == 1) for hi in H])
    H.sort()
    #
    ans = o // 2
    if o % 2:
        ans += 1
    ans += sum([int(hi != 1) for hi in H])
    print(ans)
