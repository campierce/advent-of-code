import aocd
import numpy as np
import re
data = aocd.get_data(year=2015, day=6)

lines = data.split('\n')
array = np.zeros((1000, 1000), dtype=int)
state = {'off': 0, 'on': 1}
for line in lines:
    m = re.search(r'(\w+) (\d+),(\d+) through (\d+),(\d+)', line)
    op, r0, c0, r1, c1 = m.groups()
    sr, sc = slice(int(r0), int(r1) + 1), slice(int(c0), int(c1) + 1)
    if op == 'toggle':
        array[sr, sc] ^= 1
    else:
        array[sr, sc] = state[op]
print(array.sum())
