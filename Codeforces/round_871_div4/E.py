import sys
sys.setrecursionlimit(10 ** 6)


"""
--
    Problem name: The Lakes
    Link: https://codeforces.com/contest/1829/problem/E
    Site: Codeforces
    Contest: Codeforces Round 871 (Div. 4)
    Status: Runtime Error
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


def bfs(grid, i, j, laks, curr):
    """
    Breadth first search algorithm

    Args:
        grid (list): grid to search on
        i (int): row index
        j (int): column index
        laks (list): lakes grid
        curr (int): current lake id

    Returns:
        int: current lake id
    """
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return 0

    if grid[i][j] == 0 or laks[i][j]:
        return 0

    laks[i][j] = curr

    return grid[i][j] + bfs(grid, i + 1, j, laks, curr) + \
        bfs(grid, i - 1, j, laks, curr) + bfs(grid, i, j + 1, laks, curr) + \
            bfs(grid, i, j - 1, laks, curr)


t = read()
for k in range(t):
    n, m = read_array()
    grid = [read_array() for _ in range(n)]
    laks = [[0 for _ in range(m)] for _ in range(n)]
    #
    max_depth = 0
    curr = 1
    for i in range(n):

        for j in range(m):

            if grid[i][j] == 0:
                continue

            if laks[i][j]:
                continue

            max_depth = max(max_depth, bfs(grid, i, j, laks, curr))
            curr += 1


    # print(f'Case #: {k + 1}')
    # for row in laks:
    #     print(*row)
    print(max_depth)
