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
    A = read_array()
    #
    ev, od = [], []
    for num in A:
        if num % 2:
            od.append(num)
        else:
            ev.append(num)

    #
    if sum(ev) > sum(od):
        print('YES')
    else:
        print('NO')
