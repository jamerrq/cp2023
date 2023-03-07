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
p = ''
i = 3

while len(p) < 17:

    if not i % 3:
        p += 'F'
    if not i % 5:
        p += 'B'

    i += 1


for _ in range(t):
    k = read()
    s = read(str)
    if s in p:
        print('YES')
    else:
        print('NO')
