from collections import defaultdict
from re import findall
from functools import cache
from itertools import product, count
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

def ismatch(x):
    for n42 in count():
        if len(x) < lmt or x[:lmt] not in s42:
            break
        x = x[lmt:]
    for n31 in count():
        if len(x) < lmt or x[:lmt] not in s31:
            break
        x = x[lmt:]
    return not x and n31 > 0 and n42 > n31

for k in ('42', '31'):
    termify(k)
s42, s31 = set(terms['42']), set(terms['31'])
lmt = len(min(s42, key=len))
print(sum([ismatch(x) for x in findall(r'\n([ab]+)', data)]))
