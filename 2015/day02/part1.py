from aocd import get_data
data = get_data(year=2015, day=2)

dims = [[int(s) for s in line.split('x')] for line in data.split('\n')]
ans = 0
for l, w, h in dims:
    areas = [l * w, l * h, w * h]
    ans += sum([2 * a for a in areas])
    ans += min(areas)
print(ans)
