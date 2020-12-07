import numpy as np
import re
from aocd import get_data
data = get_data(year=2015, day=6)

lines = data.split('\n')
array = np.zeros((1000, 1000), dtype=int)
state = {'off': -1, 'on': 1, 'toggle': 2}
for line in lines:
    m = re.search('(\w+) (\d+),(\d+) through (\d+),(\d+)', line)
    op, r0, c0, r1, c1 = m.groups()
    sr, sc = slice(int(r0), int(r1) + 1), slice(int(c0), int(c1) + 1)
    array[sr, sc] += state[op]
    array[array < 0] = 0
print(array.sum())
