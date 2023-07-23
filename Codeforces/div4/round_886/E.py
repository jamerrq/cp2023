import sys


"""
--
    Problem name: Cardboard for Pictures
    Link: https://codeforces.com/contest/1850/problem/E
    Site: Codeforces
    Contest: Codeforces Round # 886 (Div. 4)
    Status:
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


def solve():
    n, c = read_array()
    S = read_array()
    #
    a = 4 * n
    b = 4 * sum(S)
    c = sum([x ** 2 for x in S]) - c
    #
    s1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    s2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    #
    print(int(max(s1, s2)))


t = read()
for _ in range(t):
    solve()
