import aocd
import re
data = aocd.get_data(year=2020, day=6)

groups = [re.sub(r'\n| ', '', x) for x in data.split('\n\n')]
ans = 0
for g in groups:
    ans += len(set(g))
print(ans)
