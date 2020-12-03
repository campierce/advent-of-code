from math import prod
from aocd import get_data
data = get_data(year=2020, day=3)

matrix = [list(x) for x in data.split('\n')]
ans = []
rows = len(matrix)
cols = len(matrix[0])
deltas = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

for dr, dc in deltas:
    r = c = t = 0
    while r < rows:
        if matrix[r][c] == '#':
            t += 1
        r += dr
        c = (c + dc) % cols
    ans.append(t)

print(prod(ans))
