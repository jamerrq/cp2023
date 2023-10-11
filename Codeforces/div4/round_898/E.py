import sys


"""
--
    Problem name: Building an Aquarium
    Link: https://codeforces.com/contest/1873/problem/E
    Site: Codeforces
    Contest: Codeforces Round # 898 (Div. 4)
    Status: WA TEST 2
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


def calcular_max_depth(arr, max_w):
    # Ordenar el arreglo
    arr.sort()
    # Acumulador de agua
    agua = 0
    # Nivel del agua
    nivel = 0
    # Acumulador de piscinas
    pools = 0
    # Iterador
    i = 0

    # Mientras el iterador sea menor que el tamaño del arreglo
    # o el acumulador de agua sea menor que el máximo de agua

    while i < len(arr) and agua < max_w:
        # Opción 1: El nivel de agua es menor que el nivel del arreglo
        if agua < arr[i]:
            # Subir el nivel de agua hasta el nivel del arreglo + 1
            # y sumar 1 al acumulador de piscinas
            diff = arr[i] - agua
            nivel += diff
            pools += 1
            agua += pools * diff
        # Opción 2: El nivel de agua es mayor o igual al nivel del arreglo
        else:
            # Sumar el nivel del arreglo al acumulador de agua
            agua += arr[i]
            # Sumar 1 al acumulador de piscinas
            pools += 1
        # Incrementar el iterador
        i += 1

    return agua


def total_water_needed(arr, h):
    # suponemos que el arreglo está ordenado
    ans = 0
    for i in range(len(arr)):
        ans += max(0, h - arr[i])
    return ans


def custom_binary_search(arr, x):

    l = 0
    r = 2 * x + 1
    ans = -1

    while l <= r:

        mid = l + (r - l) // 2
        xmd = total_water_needed(arr, mid)

        if xmd <= x:
            ans = mid
            l = mid + 1

        else:
            r = mid - 1

    return ans


t = read()
for _ in range(t):
    n, max_w = read_array()
    arr = read_array()
    arr.sort()
    # print('arr', arr)
    # print('max_w', max_w)
    print(custom_binary_search(arr, max_w))
