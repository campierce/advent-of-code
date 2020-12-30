import aocd
data = aocd.get_data(year=2015, day=18)

grid = []
for line in data.split('\n'):
    grid.append([1 if ch == '#' else 0 for ch in line])

for _ in range(100):
    for r, c in ((0, 0), (0, 99), (99, 99), (99, 0)):
        grid[r][c] = 1
    temp = [[0 for _ in range(100)] for _ in range(100)]
    for r in range(100):
        for c in range(100):
            nbr = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not dr == dc == 0:
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < 100 and 0 <= cc < 100:
                            nbr += grid[rr][cc]
            if nbr == 3 or (grid[r][c] and nbr == 2):
                temp[r][c] = 1
    grid = temp

for r, c in ((0, 0), (0, 99), (99, 99), (99, 0)):
    grid[r][c] = 1
print(sum(map(sum, grid)))
