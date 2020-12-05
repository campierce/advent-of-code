import re
from aocd import get_data
data = get_data(year=2020, day=4)

temp = [re.split(' |\n', x) for x in data.split('\n\n')]
keys = [[x.split(':')[0] for x in y] for y in temp]
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
ans = 0
for k in keys:
    diff = required.difference(k)
    if not diff:
        ans += 1
print(ans)
