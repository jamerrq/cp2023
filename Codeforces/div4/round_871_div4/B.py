import sys


"""
--
    Problem name: Blank Space
    Link: https://codeforces.com/contest/1829/problem/B
    Site: Codeforces
    Contest: Codeforces Round 871 (Div. 4)
    Status: Accepted
--
"""


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def binary_search(arr, x):
    """
    return the latest position in arr such that the element at this index
    is lower or equal to the x value
    if no such element exists, it returns -1

    Args:
        arr (list): sorted list to search on
        x (int): value to compare the elements

    Returns:
        int: index of latest element lower or equal to x
    """
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
    Greatest common divisor algorithm
    https://cp-algorithms.com/algebra/euclid-algorithm.html

    Args:
        a (int): number 1
        b (int): number 2

    Returns:
        int: gcd of a and b
    """
    if not b:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    """
    Least common multiple

    Args:
        a (int): number 1
        b (int): number 2

    Returns:
        int: lcm of a and b
    """
    return a / gcd(a, b) * b



t = read()
for _ in range(t):
    n = read()
    A = read_array()
    #
    m = 0
    B = [0] * n
    #
    if A[0] == 0:
        B[0] = 1
        m = 1
    for i in range(1, n):
        if A[i] == 0:
            B[i] = B[i - 1] + 1
            m = max(m, B[i])

    print(m)