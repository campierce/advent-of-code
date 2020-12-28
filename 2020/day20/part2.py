from collections import defaultdict
from re import search
from math import sqrt
from aocd import get_data
data = get_data(year=2020, day=20)

tiles = data.split('\n\n')

# [left, top, right, bottom]
def edges(grid):
    grid = grid.split('\n')
    return [''.join(row[0] for row in grid), grid[0],
            ''.join(row[-1] for row in grid), grid[-1]]

def nodir(e):
    return min(e, e[::-1])

def flip(grid):
    grid = grid.split('\n')
    return '\n'.join(row[::-1] for row in grid)

def rotate(grid):
    grid = grid.split('\n')
    new = []
    for c in range(len(grid)):
        new.append(''.join(row[c] for row in grid)[::-1])
    return '\n'.join(new)

def orientations(grid):
    for i in range(8):
        yield grid
        grid = flip(grid)
        if i % 2 == 1:
            grid = rotate(grid)

def buildrow():
    while len(img[-1]) < COLS:
        prev = img[-1][-1]
        e = edges(prev)[2]
        nbr = next(x for x in edgetotile[nodir(e)] if x not in seen)
        seen.add(nbr)
        grid = tmap[nbr]
        for g in orientations(grid):
            if edges(g)[0] == e:
                img[-1].append(g)
                break

def ismonster(grid, r, c):
    grid = grid.split('\n')
    for dr, dc in SM:
        if grid[r+dr][c+dc] != '#':
            return False
    return True

# build maps
tmap = {}
edgetotile = defaultdict(list)
for tile in tiles:
    head, grid = tile.split('\n', 1)
    tk = int(search(r'(\d+)', head)[1])
    tmap[tk] = grid
    for e in (nodir(e) for e in edges(grid)):
        edgetotile[e].append(tk)

# init constants
COLS = int(sqrt(len(tmap)))
SM = ((0, 18),
      (1, 0), (1, 5), (1, 6), (1, 11), (1, 12), (1, 17), (1, 18), (1, 19),
      (2, 1), (2, 4), (2, 7), (2, 10), (2, 13), (2, 16))

# choose corner, build first row
seen = set()
img = [[]]
for tk, grid in tmap.items():
    if sum(len(edgetotile[nodir(e)]) for e in edges(grid)) == 6:
        seen.add(tk)
        for g in orientations(grid):
            y0, x0 = [nodir(e) for e in edges(g)[:2]]
            if len(edgetotile[y0]) == len(edgetotile[x0]) == 1:
                img[-1].append(g)
                buildrow()
                break
        break

# build the rest
while len(img) < COLS:
    prev = img[-1][0]
    e = edges(prev)[3]
    nbr = next(x for x in edgetotile[nodir(e)] if x not in seen)
    seen.add(nbr)
    grid = tmap[nbr]
    for g in orientations(grid):
        if edges(g)[1] == e:
            img.append([g])
            break
    buildrow()

# strip edges and join
actual = []
for block in img:
    temp = [grid.split('\n') for grid in block]
    for r in range(1, len(temp[0]) - 1):
        actual.append(''.join([g[r][1:-1] for g in temp]))

# look for SM
monsters = 0
for g in orientations('\n'.join(actual)):
    for r in range(len(actual) - 2):
        for c in range(len(actual) - 19):
            if ismonster(g, r, c):
                monsters += 1
    if monsters:
        break

print(g.count('#') - monsters * len(SM))
