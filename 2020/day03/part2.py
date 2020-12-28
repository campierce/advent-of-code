import aocd
data = aocd.get_data(year=2020, day=3)

grid = [list(x) for x in data.split('\n')]
rows, cols = len(grid), len(grid[0])
deltas = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

ans = 1
for dr, dc in deltas:
    r = c = t = 0
    while r < rows:
        if grid[r][c] == '#':
            t += 1
        r += dr
        c = (c + dc) % cols
    ans *= t

print(ans)
