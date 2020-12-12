import re
from aocd import get_data
data = get_data(year=2020, day=4)

groups = [re.split(r' |\n', x) for x in data.split('\n\n')]
pairs = [{x[0]: x[1] for x in (y.split(':') for y in z)} for z in groups]
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def is_valid(p):
    return ((1920 <= int(p['byr']) <= 2002) and
            (2010 <= int(p['iyr']) <= 2020) and
            (2020 <= int(p['eyr']) <= 2030) and
            ((re.match(r'^[0-9]{3}cm', p['hgt']) and
                       150 <= int(p['hgt'][:3]) <= 193) or
            (re.match(r'^[0-9]{2}in', p['hgt']) and
                       59 <= int(p['hgt'][:2]) <= 76)) and
            (re.match(r'^#[0-9a-f]{6}', p['hcl'])) and
            (p['ecl'] in colors) and
            (re.match(r'^[0-9]{9}$', p['pid'])))

ans = 0
for p in pairs:
    if not required.difference(p.keys()) and is_valid(p):
        ans += 1
print(ans)
