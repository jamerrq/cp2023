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
    n, k = read_array()
    s = read(str)
    #
    m = {}
    M = {}
    d = set()
    for char in s:
        mc = char.lower()
        if char.islower():
            m[mc] = m.get(mc, 0) + 1
        else:
            M[mc] = M.get(mc, 0) + 1

        d.add(mc)

    # print(m, M)
    ans = 0
    for char in d:
        mc, Mc = m.get(char, 0), M.get(char, 0)

        if mc != Mc:
            diff = abs(mc - Mc)
            to_up = min(diff // 2, k)
            ans += min(mc, Mc) + to_up
            k -= to_up

        else:
            ans += min(mc, Mc)

        # print(char, ans)

    print(ans)
