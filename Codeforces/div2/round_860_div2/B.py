import sys


"""
--
    Problem name: Three Sevens
    Link: https://codeforces.com/contest/1798/problem/B
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

    m = read()
    days = {}
    last = {}

    for i in range(m):
        n = read()
        A = read_array()
        days[i] = A
        for ai in A:
            last[ai] = i

    ans = []
    idx = 0
    lvl = -1
    vls = [(key, value) for key, value in last.items()]
    vls.sort(key = lambda x : x[1])

    while idx < len(vls):

        if(vls[idx][1] == lvl + 1):
            lvl += 1
            ans.append(vls[idx][0])

        idx += 1

    if len(ans) == m:
        print(*ans)
    else:
        print(-1)
