import sys


"""
--
    Problem name: Conveyor Belts
    Link: https://codeforces.com/contest/1811/problem/B
    Site: Codeforces
    Contest: Codeforces Round # 863 (Div. 3)
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
    n, x1, y1, x2, y2 = read_array()
    #
    x1_lvl = x1 if x1 <= n / 2 else n - x1 + 1
    y1_lvl = y1 if y1 <= n / 2 else n - y1 + 1
    x2_lvl = x2 if x2 <= n / 2 else n - x2 + 1
    y2_lvl = y2 if y2 <= n / 2 else n - y2 + 1
    ribbon_1 = min(x1_lvl, y1_lvl)
    ribbon_2 = min(x2_lvl, y2_lvl)
    #
    print(abs(ribbon_1 - ribbon_2))
