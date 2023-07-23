import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def binary_search(arr, x):
    i, j = 0, len(arr) - 1
    ans = -1
    while i <= j:

        mid = i + (j - i) // 2
        xmd = arr[mid]

        if xmd <= x:
            ans = mid
            i = mid + 1

        else:
            j = mid - 1

    return ans


t = read()
for _ in range(t):
    n = read()
    A = read_array()
    #
    odds = []
    even = []
    for i in range(n):
        ai = A[i]
        if ai % 2:
            odds.append(i)
        else:
            even.append(i)

    #
    no, ne = len(odds), len(even)
    if no >= 3:
        print('YES')
        print(' '.join([str(x + 1) for x in odds[:3]]))

    elif no == 2 or no == 1:
        if ne == 1:
            print('NO')
        else:
            print('YES')
            print(' '.join([str(x + 1) for x in odds[:1] + even[:2]]))

    else:
        print('NO')
