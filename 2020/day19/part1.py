import aocd
import collections
import functools as ft
import itertools as it
import re
data = aocd.get_data(year=2020, day=19)

cfg, terms = collections.defaultdict(list), collections.defaultdict(list)
for k, v in re.findall(r'(\d+): (.+)', data):
    if v.startswith('"'):
        terms[k].append(v[1])
    else:
        for opt in v.split(' | '):
            cfg[k].append(opt.split(' '))

@ft.cache
def termify(k):
    for opt in cfg[k]:
        for k2 in opt:
            termify(k2) if k2 in cfg else None
    for opt in cfg[k]:
        for p in it.product(*[terms[k2] for k2 in opt]):
            terms[k].append(''.join(p))

termify('0')
valid = set(terms['0'])
print(sum((1 for x in re.findall(r'\n([ab]+)', data) if x in valid)))
