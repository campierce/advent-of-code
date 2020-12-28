import aocd
import collections
data = aocd.get_data(year=2020, day=24)

deltas = {'e': (1, -1, 0), 'w': (-1, 1, 0),
    'se': (0, -1, 1), 'sw': (-1, 0, 1),
    'ne': (1, 0, -1), 'nw': (0, 1, -1)}

turned = set()
for line in data.split('\n'):
    i = x = y = z = 0
    while i < len(line):
        if line[i] in ('e', 'w'):
            dx, dy, dz = deltas[line[i]]
            i += 1
        else:
            dx, dy, dz = deltas[line[i:i+2]]
            i += 2
        x, y, z = x+dx, y+dy, z+dz
    dst = (x, y, z)
    if dst in turned:
        turned.remove(dst)
    else:
        turned.add(dst)

for _ in range(100):
    nbr = collections.defaultdict(int)
    for x, y, z in turned:
        for dx, dy, dz in deltas.values():
            nbr[(x+dx, y+dy, z+dz)] += 1
    new = set()
    for k, v in nbr.items():
        if ((k not in turned and v == 2) or
            (k in turned and v in (1, 2))):
            new.add(k)
    turned = new

print(len(turned))
