import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def binary_search(arr, x):
    #
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
    https://cp-algorithms.com/algebra/euclid-algorithm.html
    """
    if not b:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    return a / gcd(a, b) * b



t = read()
for _ in range(t):
    n, m, i1, j1, i2, j2, d = read_array(str)
    n, m, i1, j1, i2, j2 = map(int, [n, m, i1, j1, i2, j2])
    #
    vis = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    dir = {
        "DL" : 0,
        "DR" : 2,
        "UR" : 3,
        "UL" : 1
    }
    #
    d = dir[d]
    i, j = i1 - 1, j1 - 1
    boun = 0
    ans = -1
    while not vis[i][j][d]:

        if i == i2 - 1 and j == j2 - 1:
            ans = boun
            break
        na = 0
        if d % 2 == 1 and i == 0:
            d  -= 1
            na += 1
        if d % 2 == 0 and i == n - 1:
            d += 1
            na += 1
        if d >= 2 and j == m - 1:
            d -= 2
            na += 1
        if d < 2 and j == 0:
            d += 2
            na += 1

        boun += min(1, na)

        if vis[i][j][d]:
            break

        vis[i][j][d] = True
        if d % 2 == 1:
            i -= 1
        else:
            i += 1
        if d >= 2:
            j += 1
        else:
            j -= 1

    print(ans)
