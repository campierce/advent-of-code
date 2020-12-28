import aocd
data = aocd.get_data(year=2020, day=6)

groups = [[set(x) for x in y.split('\n')] for y in data.split('\n\n')]
ans = 0
for g in groups:
    ans += len(g[0].intersection(*g[1:]))
print(ans)
