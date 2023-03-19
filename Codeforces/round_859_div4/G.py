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


"""
Original solution by MrSossa
https://codeforces.com/contest/1807/submission/198205631
"""
t = read()
for _ in range(t):
    n = read()
    C = read_array()
    #
    C.sort()
    ans = "YES"
    if C[0] != 1:
        ans = "NO"
    else:
        sum = 1
        for i in range(1, n):
            if C[i] <= sum:
                sum += C[i]
            else:
                ans = 'NO'
                break

    print(ans)
