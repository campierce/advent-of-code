import aocd
data = aocd.get_data(year=2015, day=3)

moves = {'^': (1, 0), '>': (0, 1), 'v': (-1, 0), '<': (0, -1)}
seen = set([(0, 0)])
r1 = c1 = r2 = c2 = 0
for i, char in enumerate(data):
    dr, dc = moves[char]
    if i % 2 == 0:
        r1 += dr
        c1 += dc
        seen.add((r1, c1))
    else:
        r2 += dr
        c2 += dc
        seen.add((r2, c2))
print(len(seen))
