import sys


def read(func=int):
    return func(sys.stdin.readline().strip())


def read_array(func=int):
    return list(map(func, read(str).split()))


t = read()
for _ in range(t):

    n, s, r = read_array()
    max_dice = s - r
    dices = [max_dice]
    approx = r // (n - 1)
    dices.extend([approx] * (n - 1))
    left_sum = s - sum(dices)
    idx = 1

    while left_sum:
        idx = max(1, idx % n)
        dices[idx] += 1
        left_sum -= 1
        idx += 1

    print(' '.join([str(dice) for dice in dices]))
