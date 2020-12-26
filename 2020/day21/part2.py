import re
from collections import defaultdict
from aocd import get_data
data = get_data(year=2020, day=21)

agenmap = {}
for x, y in re.findall(r'([a-z ]+) \(contains ([a-z, ]+)\)', data):
    for a in y.split(', '):
        if a not in agenmap:
            agenmap[a] = set(x.split())
        else:
            agenmap[a] &= set(x.split())

inv = defaultdict(list)
for k, v in agenmap.items():
    for gib in v:
        inv[gib].append(k)

oo = {}
used = set()
while len(oo) < len(inv):
    for gib, agen in inv.items():
        opts = [x for x in agen if x not in used]
        if len(opts) == 1:
            oo[gib] = opts[0]
            used.add(opts[0])

ans = list(sorted(oo.keys(), key=lambda x: oo[x]))
print(','.join([x for x in ans]))
