import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def binary_search(arr, x):
    """
    return the position of the last element greater than or equal to x
    """
    i, j = 0, len(arr) - 1
    ans = -1
    while i <= j:

        mid = i + (j - i) // 2

        xmd = arr[mid]

        # print(i, j, xmd)

        if xmd <= x:
            ans = mid
            i = mid + 1
            # print('here')

        else:
            j = mid - 1


    return ans




t = read()
for _ in range(t):
    n = read()
    A = read_array()
    B = read_array()
    #
    add = [0] * (n + 1)
    prf = [0] * (n + 1)
    #
    for i in range(1, n + 1):
        prf[i] = prf[i - 1] + B[i - 1]

    # print(prf)
    #
    cnt = [0] * (n + 1)
    for i in range(n):
        j = binary_search(prf, A[i] + prf[i])
        # print(j)
        cnt[i] += 1
        cnt[j] -= 1
        add[j] += A[i] - prf[j] + prf[i]

    ans = [0] * n
    # print(cnt)
    for i in range(n):
        ans[i] = cnt[i] * B[i] + add[i]
        cnt[i  + 1] += cnt[i]

    print(' '.join([str(x) for x in ans]))
    # print(cnt)
