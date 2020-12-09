from itertools import combinations
from aocd import get_data
data = get_data(year=2020, day=9)

lines = [int(x) for x in data.split('\n')]

for i in range(25, len(lines)):
    seen = set([x + y for x, y in list(combinations(lines[i-25:i], 2))])
    if lines[i] not in seen:
        print(lines[i])
        break
