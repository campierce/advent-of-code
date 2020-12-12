from aocd import get_data
data = get_data(year=2020, day=3)

grid = [list(x) for x in data.split('\n')]
rows, cols = len(grid), len(grid[0])
r = c = 0
dr, dc = 1, 3

ans = 0
while r < rows:
    if grid[r][c] == '#':
        ans += 1
    r += dr
    c = (c + dc) % cols

print(ans)
