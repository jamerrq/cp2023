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
    n = read()
    s = read(str)
    m, e, o, w = [False] * 4
    st = -1
    ans = True
    for i in range(n):
        ci = s[i].lower()
        if st == -1:
            if ci == 'm':
                st += 1
            else:
                ans = False
                break
        elif st == 0:
            if ci == 'e':
                st += 1
            else:
                if ci == 'm':
                    continue
                else:
                    ans = False
                    break

        elif st == 1:
            if ci == 'o':
                st += 1
            else:
                if ci == 'e':
                    continue
                else:
                    ans = False
                    break

        elif st == 2:
            if ci == 'w':
                st += 1
            else:
                if ci == 'o':
                    continue
                else:
                    ans = False
                    break

        elif st == 3:
            if ci == 'w':
                continue
            else:
                ans = False
                break


    if ans and st == 3:
        print('YES')
    else:
        print('NO')
