import aocd
import collections
data = aocd.get_data(year=2020, day=22)

px = data.split('\n\n')
p1 = collections.deque([int(x) for x in px[0].split('\n')[1:]])
p2 = collections.deque([int(x) for x in px[1].split('\n')[1:]])

while p1 and p2:
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)

wp = reversed(p1 if p1 else p2)
print(sum([(i + 1) * c for i, c in enumerate(wp)]))
