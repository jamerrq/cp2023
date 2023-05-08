import sys


"""
--
    Problem name: Forever Winter
    Link: https://codeforces.com/contest/1829/problem/F
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
    n, m = read_array()
    #
    conn  = {}
    #
    for _ in range(m):
        u, v = read_array()
        #
        conn[u] = conn.get(u, 0) + 1
        conn[v] = conn.get(v, 0) + 1

    #
    values = [x for x in conn.values() if x != 1]
    values.sort(key=lambda x: -x)
    a, b, c = values[0], values[len(values) // 2], values[-1]
    #
    if a == b:
        print(c, a - 1)
    else:
        print(a, b - 1)
