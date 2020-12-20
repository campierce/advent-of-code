from re import findall, search
from itertools import chain
from collections import defaultdict
from math import prod
from aocd import get_data
data = get_data(year=2020, day=16)

valid = set()
fields = []
temp = findall(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', data)
deps = [i for i, x in enumerate(temp) if x[0].startswith('departure')]
for x1, y1, x2, y2 in [map(int, x[1:]) for x in temp]:
    valid.update(list(range(x1, y1+1)), list(range(x2, y2+1)))
    fields.append(set(chain(list(range(x1, y1+1)), list(range(x2, y2+1)))))

temp = data.split('nearby tickets:\n')[1]
tix = [[int(x) for x in y.split(',')] for y in temp.split('\n')]
possible = defaultdict(list)
for pos in range(len(tix[0])):
    col = set([t[pos] for t in tix if t[pos] in valid])
    for fid, f in enumerate(fields):
        if len(col.difference(f)) == 0:
            possible[fid].append(pos)

ans = []
seen = set()
for fid in sorted(possible.keys(), key=lambda k: len(possible[k])):
    for pos in possible[fid]:
        if pos not in seen:
            seen.add(pos)
            if fid in deps:
                ans.append(pos)

temp = search(r'your ticket:\n([0-9,]+)', data)[1]
mine = [int(x) for x in temp.split(',')]
print(prod([mine[i] for i in ans]))
