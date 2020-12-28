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

def ismatch(x):
    for n42 in it.count():
        if len(x) < lmt or x[:lmt] not in s42:
            break
        x = x[lmt:]
    for n31 in it.count():
        if len(x) < lmt or x[:lmt] not in s31:
            break
        x = x[lmt:]
    return not x and n31 > 0 and n42 > n31

for k in ('42', '31'):
    termify(k)
s42, s31 = set(terms['42']), set(terms['31'])
lmt = len(min(s42, key=len))
print(sum((ismatch(x) for x in re.findall(r'\n([ab]+)', data))))
