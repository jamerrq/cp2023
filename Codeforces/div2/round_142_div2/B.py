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
    A = read_array()
    #
    ans = 1
    if A[0]:
        ans = A[0] + min(A[1],A[2]) * 2 + min(A[0] + 1, abs(A[1] - A[2]) + A[3])

    print(ans)
