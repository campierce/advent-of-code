import itertools as it
from aocd import get_data
data = get_data(year=2020, day=14)

lines = data.split('\n')

mask = None
mem = {}
for line in lines:
    op, arg = line.split(' = ')
    if op == 'mask':
        mask = list(reversed(arg))
    else:
        k = int(op[4:-1])
        sb = []
        for i in range(36):
            if mask[i] == 'X':
                sb.append('{}')
            elif (mask[i] == '1' or
                  k & (1 << i)):
                sb.append('1')
            else:
                sb.append('0')

        s = ''.join(reversed(sb))
        for t in it.product([0, 1], repeat=mask.count('X')):
            temp = s.format(*t)
            mem[int(temp, 2)] = int(arg)

print(sum(mem.values()))
