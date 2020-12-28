import aocd
import collections
import re
data = aocd.get_data(year=2020, day=2)

lines = data.split('\n')
ans = 0
for line in lines:
    m = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, pw = m.groups()
    c = collections.Counter(pw)
    if int(lo) <= c.get(char, -1) <= int(hi):
        ans += 1
print(ans)
