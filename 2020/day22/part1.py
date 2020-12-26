import re
from collections import deque
from aocd import get_data
data = get_data(year=2020, day=22)

px = data.split('\n\n')
p0 = deque([int(x) for x in px[0].split('\n')[1:]])
p1 = deque([int(x) for x in px[1].split('\n')[1:]])

while p0 and p1:
    c0 = p0.popleft()
    c1 = p1.popleft()
    if c0 > c1:
        p0.append(c0)
        p0.append(c1)
    else:
        p1.append(c1)
        p1.append(c0)

wp = reversed(p0 if p0 else p1)
print(sum([(i + 1) * c for i, c in enumerate(wp)]))
