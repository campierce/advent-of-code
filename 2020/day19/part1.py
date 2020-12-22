from collections import defaultdict
from re import findall
from functools import cache
from itertools import product
from aocd import get_data
data = get_data(year=2020, day=19)

cfg, terms = defaultdict(list), defaultdict(list)
for k, v in findall(r'(\d+): (.+)', data):
    if v.startswith('"'):
        terms[k].append(v[1])
    else:
        for opt in v.split(' | '):
            cfg[k].append(opt.split(' '))

@cache
def termify(k):
    for opt in cfg[k]:
        for k2 in opt:
            termify(k2) if k2 in cfg else None
    for opt in cfg[k]:
        for p in product(*[terms[k2] for k2 in opt]):
            terms[k].append(''.join(p))

termify('0')
valid = set(terms['0'])
print(len([1 for x in findall(r'\n([ab]+)', data) if x in valid]))
