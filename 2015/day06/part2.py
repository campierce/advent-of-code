from aocd import get_data
data = get_data(year=2015, day=6)

def get_instruction(arr):
    action = arr[-4]
    r0, c0 = [int(x) for x in arr[-3].split(',')]
    r1, c1 = [int(x) for x in arr[-1].split(',')]
    return (action, r0, c0, r1, c1)

lines = [x.split(' ') for x in data.split('\n')]
grid = [[0 for _ in range(1000)] for _ in range(1000)]
for line in lines:
    action, r0, c0, r1, c1 = get_instruction(line)
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            if action == 'on':
                grid[r][c] += 1
            elif action == 'off':
                grid[r][c] = max(grid[r][c] - 1, 0)
            else:
                grid[r][c] += 2
print(sum(map(sum, grid)))
