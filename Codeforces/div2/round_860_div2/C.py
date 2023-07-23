import sys


"""
--
    Problem name: Candy Store
    Link: https://codeforces.com/contest/1798/problem/C
    Site: Codeforces
    Contest: Codeforces Round 860 (Div. 2)
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
    A, B = [], []
    for _ in range(n):
        ai, bi = read_array()
        A.append(ai)
        B.append(bi)
    #
    g = 0
    l = 1
    a = 1 # last one
    for i in range(n):
        g = gcd(g, A[i] * B[i])
        l = lcm(l, B[i])
        if g % l:
            # reset current solution
            a += 1
            g = A[i] * B[i]
            l = B[i]

    print(a)
