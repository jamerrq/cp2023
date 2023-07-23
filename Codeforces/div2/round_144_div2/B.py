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
    a = read(str)
    b = read(str)
    if a[0] == b[0]:
        print('YES')
        print(f'{a[0]}*')
    elif a[-1] == b[-1]:
        print('YES')
        print(f'*{a[-1]}')
    else:
        fnd = False
        wld = ''
        for i in range(len(a) - 1):
            subi = a[i] + a[i + 1]
            if subi in b:
                fnd = True
                wld = subi
                break

        if fnd:
            print('YES')
            print(f'*{wld}*')
        else:
            print('NO')
