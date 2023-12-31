import sys


"""
--
    Problem name: A. 2023
    Link: https://codeforces.com/contest/1916/problem/A
    Site: Codeforces
    Contest: Good Bye 2023
    Status:
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
    _, k = read_array()
    B = read_array()
    #
    mult = 1
    for bi in B: mult *= bi
    if 2023 % mult != 0:
        print("NO")
        return
    #
    divs = [1, 7, 17, 119, 289, 2023]
    curr = 2023 // mult
    i = 5
    ans = []
    while curr > 1 and len(ans) < k:
        if curr % divs[i] == 0:
            ans.append(divs[i])
            curr //= divs[i]
        else:
            i -= 1
    #
    while len(ans) < k:
        ans.append(1)
    #
    print("YES")
    print(*ans)


t = read()
for _ in range(t):
    solve()
