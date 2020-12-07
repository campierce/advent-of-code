from aocd import get_data
data = get_data(year=2020, day=3)

matrix = [list(x) for x in data.split('\n')]
rows, cols = len(matrix), len(matrix[0])
r = c = 0
dr, dc = 1, 3

ans = 0
while r < rows:
    if matrix[r][c] == '#':
        ans += 1
    r += dr
    c = (c + dc) % cols

print(ans)
