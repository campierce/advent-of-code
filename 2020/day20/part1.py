import re
from collections import Counter
from aocd import get_data
data = get_data(year=2020, day=20)

tiles = data.split('\n\n')

outer, borders = {}, []
for t in tiles:
    head, body = t.split('\n', 1)
    tkey = int(re.search(r'(\d+)', head)[1])
    grid = body.split('\n')
    bord = []
    for i in (-1, 0):
        bord.append(grid[i])
        bord.append(''.join([row[i] for row in grid]))
    norm = [sorted([b, ''.join(reversed(b))])[0] for b in bord]
    outer[tkey] = norm
    borders.extend(norm)

ctr = Counter(borders)
ans = 1
for tkey, norm in outer.items():
    if sum([ctr[b] for b in norm]) == 6:
        ans *= tkey
print(ans)
