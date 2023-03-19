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


def make_query(i, j, B):
    print(f'? {j - i + 1} ' + ' '.join([str(x + 1) for x in range(i, j + 1)]))
    sys.stdout.flush()
    x = read()
    return not (x == B[j + 1] - B[i])


t = read()
for _ in range(t):
    n = read()
    A = read_array()
    qs = 0
    #
    B = [0] * (n + 1)
    for i in range(n):
        B[i + 1] = B[i] + A[i]
    #
    i = 0
    j = n // 2
    #
    minI, maxJ = 0, n - 1
    while i != j:

        x = make_query(i, j, B)
        if x:
            if i == j - 1:
                break
            minI = i
            maxJ = j
            j = minI + (maxJ - minI) // 2
        else:
            minI = j + 1
            i = minI
            j = minI + (maxJ - minI + 1) // 2


    if i != j:
        qs += 1
        x = make_query(i, i, B)
        if x:
            print(f'! {i + 1}')
            sys.stdout.flush()
        else:
            print(f'! {j + 1}')
            sys.stdout.flush()
    else:
        print(f'! {i + 1}')
        sys.stdout.flush()

