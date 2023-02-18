import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


def binary_search(arr, x):
    """
    return the position of the last element greater than or equal to x
    special thanks to Errichto
    https://www.youtube.com/watch?v=GU7DpgHINWQ&t=642s
    """
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
