import re
from aocd import get_data
data = get_data(year=2020, day=4)

temp = [re.split(' |\n', x) for x in data.split('\n\n')]
pairs = [{x[0]: x[1] for x in (y.split(':') for y in z)} for z in temp]
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def is_valid(k, v):
    if k == 'byr':
        # don't actually need to check that it's four digits
        return 1920 <= int(v) <= 2002
    elif k == 'iyr':
        return 2010 <= int(v) <= 2020
    elif k == 'eyr':
        return 2020 <= int(v) <= 2030
    elif k == 'hgt':
        return (re.match('^[0-9]{3}cm', v) and 150 <= int(v[:3]) <= 193 or
                re.match('^[0-9]{2}in', v) and 59 <= int(v[:2]) <= 76)
    elif k == 'hcl':
        return re.match('^#[0-9a-f]{6}', v)
    elif k == 'ecl':
        return v in colors
    elif k == 'pid':
        return re.match('^[0-9]{9}$', v)
    return True

ans = 0
for p in pairs:
    diff = required.difference(p.keys())
    if not diff:
        for k, v in p.items():
            if not is_valid(k, v):
                break
        else:
            ans += 1
print(ans)
