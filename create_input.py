contest = "Codeforces/round_859_div4"
file = open(f'{contest}/in', 'w')
#
n = 200000
t = 1
#
file.write(f'{t}\n')
for _ in range(t):

    file.write(f'{n}\n')
    arr = [n] * n
    file.write(' '.join([str(x) for x in arr]) + '\n')
