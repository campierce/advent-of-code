import aocd
import re
data = aocd.get_data(year=2020, day=4)

groups = [re.split(r' |\n', x) for x in data.split('\n\n')]
keys = [[x.split(':')[0] for x in y] for y in groups]
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
ans = 0
for k in keys:
    if not required.difference(k):
        ans += 1
print(ans)
