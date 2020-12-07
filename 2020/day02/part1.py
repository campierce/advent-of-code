import re
from collections import Counter
from aocd import get_data
data = get_data(year=2020, day=2)

lines = data.split('\n')
ans = 0
for line in lines:
    m = re.search('(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, pw = m.groups()
    c = Counter(pw)
    if int(lo) <= c.get(char, -1) <= int(hi):
        ans += 1
print(ans)
