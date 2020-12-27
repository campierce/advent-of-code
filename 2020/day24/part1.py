from aocd import get_data
data = get_data(year=2020, day=24)

# offset coordinates:
# https://www.redblobgames.com/grids/hexagons/
delta = {'e': (1, -1, 0), 'w': (-1, 1, 0),
    'se': (0, -1, 1), 'sw': (-1, 0, 1),
    'ne': (1, 0, -1), 'nw': (0, 1, -1)}

turned = set()
for line in data.split('\n'):
    i = x = y = z = 0
    while i < len(line):
        if line[i] in ('e', 'w'):
            dx, dy, dz = delta[line[i]]
            i += 1
        else:
            dx, dy, dz = delta[line[i:i+2]]
            i += 2
        x, y, z = x+dx, y+dy, z+dz
    dst = (x, y, z)
    if dst in turned:
        turned.remove(dst)
    else:
        turned.add(dst)

print(len(turned))
