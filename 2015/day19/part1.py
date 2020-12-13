import re
from collections import defaultdict
from aocd import get_data
data = get_data(year=2015, day=19)

lines = data.split('\n')
m0 = re.findall(r'[A-Z][a-z]*', lines[-1])
expansions = defaultdict(list)
for x in [x.split(' => ') for x in lines[:-2]]:
    expansions[x[0]].append(x[1])

ans = set()
for i, char in enumerate(m0):
    for s in expansions[char]:
        m1 = m0[:i] + [s] + m0[i+1:]
        ans.add(''.join(m1))
print(len(ans))
