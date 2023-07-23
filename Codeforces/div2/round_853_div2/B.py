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
    s = read(str)
    #
    A = [0] * (n // 2)
    for i in range(n // 2):
        if s[i] != s[-i-1]:
            A[i] = 1


    one = False
    cnt = 0
    for i in range(n // 2):

        if one:
            if A[i]:
                continue
            else:
                one = False

        else:
            if A[i]:
                cnt += 1
                one = True
                continue
            else:
                continue


    if cnt < 2:
        print('Yes')
    else:
        print('No')
