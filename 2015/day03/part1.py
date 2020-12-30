import aocd
data = aocd.get_data(year=2015, day=3)

moves = {'^': (1, 0), '>': (0, 1), 'v': (-1, 0), '<': (0, -1)}
seen = set([(0, 0)])
r = c = 0
for char in data:
    dr, dc = moves[char]
    r += dr
    c += dc
    seen.add((r, c))
print(len(seen))
