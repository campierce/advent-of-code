from copy import deepcopy
from aocd import get_data
data = get_data(year=2020, day=11)

lines = data.split('\n')
R = len(lines)
C = len(lines[0])
grid = [[0 for _ in range(C)] for _ in range(R)]
floor = set()
for r in range(R):
    for c in range(C):
        if lines[r][c] == '.':
            floor.add((r, c))

while True:
    stable = True
    temp = deepcopy(grid)
    for r in range(R):
        for c in range(C):
            if (r, c) in floor:
                continue
            nbr = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not dr == dc == 0:
                        rr, cc = r + dr, c + dc
                        while 0 <= rr < R and 0 <= cc < C:
                            if (rr, cc) not in floor:
                                nbr += grid[rr][cc]
                                break
                            rr += dr
                            cc += dc
            if grid[r][c] == 0 and nbr == 0:
                temp[r][c] = 1
                stable = False
            elif grid[r][c] == 1 and nbr >= 5:
                temp[r][c] = 0
                stable = False
    if stable:
        break
    grid = temp

print(sum(map(sum, grid)))