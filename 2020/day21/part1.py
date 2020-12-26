import re
from collections import defaultdict
from aocd import get_data
data = get_data(year=2020, day=21)

ing = defaultdict(int)
agenmap = {}
for x, y in re.findall(r'([a-z ]+) \(contains ([a-z, ]+)\)', data):
    x = x.split()
    for i in x:
        ing[i] += 1
    for a in y.split(', '):
        if a not in agenmap:
            agenmap[a] = set(x)
        else:
            agenmap[a] &= set(x)

illegal = set()
illegal = illegal.union(*agenmap.values())
print(sum([v for k, v in ing.items() if k not in illegal]))
