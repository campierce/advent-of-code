from collections import defaultdict
from itertools import product
from aocd import get_data
data = get_data(year=2020, day=17)

grid = defaultdict(int)

for x, row in enumerate(data.split('\n')):
    for y, char in enumerate(row):
        if char == '#':
            grid[(x, y, 0)] = 1

for _ in range(6):
    neighbors = defaultdict(int)
    for coords, is_active in grid.items():
        if is_active:
            for delta in product([-1, 0, 1], repeat=3):
                if any(delta):
                    neighbors[tuple(map(sum, zip(coords, delta)))] += 1
    new_grid = defaultdict(int)
    for coords, num in neighbors.items():
        if num == 3 or (grid[coords] and num == 2):
            new_grid[coords] = 1
    grid = new_grid

print(sum(grid.values()))
