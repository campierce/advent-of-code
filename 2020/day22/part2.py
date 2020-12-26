import re
from collections import deque
from aocd import get_data
data = get_data(year=2020, day=22)

px = data.split('\n\n')
p0 = deque([int(x) for x in px[0].split('\n')[1:]])
p1 = deque([int(x) for x in px[1].split('\n')[1:]])

def p0wins(p0, p1):
    seen = set()
    while p0 and p1:
        # check for repeat
        state = (tuple(p0), tuple(p1))
        if state in seen:
            return True
        seen.add(state)
        # prep for round
        c0 = p0.popleft()
        c1 = p1.popleft()
        # get round winner
        if c0 <= len(p0) and c1 <= len(p1):
            np0 = deque(list(p0)[:c0])
            np1 = deque(list(p1)[:c1])
            p0w = p0wins(np0, np1)
        else:
            p0w = c0 > c1
        # move cards
        if p0w:
            p0.append(c0)
            p0.append(c1)
        else:
            p1.append(c1)
            p1.append(c0)
    return True if p0 else False

p0wins(p0, p1)
wp = reversed(p0 if p0 else p1)
print(sum([(i + 1) * c for i, c in enumerate(wp)]))
