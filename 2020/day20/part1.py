import aocd
import collections
import re
data = aocd.get_data(year=2020, day=20)

tiles = data.split('\n\n')

def edges(grid):
    grid = grid.split('\n')
    return [''.join(row[0] for row in grid), grid[0],
            ''.join(row[-1] for row in grid), grid[-1]]

def nodir(e):
    return min(e, e[::-1])

tmap = {}
edgetotile = collections.defaultdict(list)
for tile in tiles:
    head, grid = tile.split('\n', 1)
    tk = int(re.search(r'(\d+)', head)[1])
    tmap[tk] = grid
    for e in (nodir(e) for e in edges(grid)):
        edgetotile[e].append(tk)

ans = 1
for tk, grid in tmap.items():
    if sum(len(edgetotile[nodir(e)]) for e in edges(grid)) == 6:
        ans *= tk
print(ans)
