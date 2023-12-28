import sys


"""
--
    Problem name: Romantic Glasses
    Link: https://codeforces.com/contest/1915/problem/E
    Site: Codeforces
    Contest: Codeforces Round # 918 (Div. 4)
    Status: Accepted
--
"""


def read(func=int):
    """read from stdint and apply func to it

    Args:
        func (function, optional): function to apply to the input.
        Defaults to int.

    Returns:
        element: element read from stdin
    """
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    """read a list of elements from stdin

    Args:
        func (function, optional): function to apply to the input.
        Defaults to int.

    Returns:
        list: list of elements read from stdin
    """
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


def solve():
    n = read()
    A = read_array()
    O = [0] * (n + 1) # pd: not neccessary to use a list,
    E = [0] * (n + 1) # a cumulative sum is enough
    M = {}
    #
    E[1] = A[0]
    ans = False
    for i in range(n):
        if i % 2:
            E[i + 1] = E[i] + A[i]
            O[i + 1] = O[i]
        else:
            O[i + 1] = O[i] + A[i]
            E[i + 1] = E[i]

        o_minus_e = O[i + 1] - E[i + 1]
        if o_minus_e in M or o_minus_e == 0:
            ans = True
            break
        else:
            M[o_minus_e] = True

    if ans:
        print('YES')
    else:
        print('NO')


t = read()
for _ in range(t):
    solve()
