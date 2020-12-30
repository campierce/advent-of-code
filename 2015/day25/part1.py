import aocd
import re
data = aocd.get_data(year=2015, day=25)

r, c = [int(x) for x in re.findall(r'[0-9]+', data)]
r0 = c + r - 1
cells = (r0 ** 2 + r0) // 2 - r
ans = 20151125
for _ in range(cells):
    ans *= 252533
    ans %= 33554393
print(ans)
