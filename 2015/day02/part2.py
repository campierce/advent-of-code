from aocd import get_data
data = get_data(year=2015, day=2)

dims = [[int(s) for s in line.split('x')] for line in data.split('\n')]
ans = 0
for l, w, h in dims:
    ans += sum([2 * x for x in (l, w, h)])
    ans -= 2 * (max(l, w, h))
    ans += l * w * h
print(ans)
