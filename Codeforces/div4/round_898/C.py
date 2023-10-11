import sys


"""
--
    Problem name: Target Practice
    Link: https://codeforces.com/contest/1873/problem/C
    Site: Codeforces
    Contest: Codeforces Round #
    Status: AC
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


t = read()
for _ in range(t):
    matrix = [read(str) for _ in range(10)]
    ans = 0
    # by rows
    for i in range(10):
        row = matrix[i]
        for j in range(10):
            if row[j] == 'X':
                if i == 0 or i == 9:
                    ans += 1
                elif i == 1 or i == 8:
                    if j == 0 or j == 9:
                        ans += 1
                    else:
                        ans += 2
                if i == 2 or i == 7:
                    if j == 0 or j == 9:
                        ans += 1
                    elif j == 1 or j == 8:
                        ans += 2
                    else:
                        ans += 3
                if i == 3 or i == 6:
                    if j == 0 or j == 9:
                        ans += 1
                    elif j == 1 or j == 8:
                        ans += 2
                    elif j == 2 or j == 7:
                        ans += 3
                    else:
                        ans += 4
                if i == 4 or i == 5:
                    if j == 0 or j == 9:
                        ans += 1
                    elif j == 1 or j == 8:
                        ans += 2
                    elif j == 2 or j == 7:
                        ans += 3
                    elif j == 3 or j == 6:
                        ans += 4
                    else:
                        ans += 5

    print(ans)
