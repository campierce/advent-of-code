import re
from aocd import get_data
data = get_data(year=2020, day=2)

lines = data.split('\n')
ans = 0
for line in lines:
    m = re.search('(\d+)-(\d+) (\w): (\w+)', line)
    lo, hi, char, pw = m.groups()
    if (pw[int(lo)-1] == char) ^ (pw[int(hi)-1] == char):
        ans += 1
print(ans)
