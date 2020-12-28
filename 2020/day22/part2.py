from collections import deque
from aocd import get_data
data = get_data(year=2020, day=22)

px = data.split('\n\n')
p1 = deque([int(x) for x in px[0].split('\n')[1:]])
p2 = deque([int(x) for x in px[1].split('\n')[1:]])

def combat(p1, p2):
    seen = set()
    while p1 and p2:
        # check for repeat
        state = (tuple(p1), tuple(p2))
        if state in seen:
            return 1
        seen.add(state)
        # prep for round
        c1 = p1.popleft()
        c2 = p2.popleft()
        # get round winner
        if c1 <= len(p1) and c2 <= len(p2):
            np1 = deque(list(p1)[:c1])
            np2 = deque(list(p2)[:c2])
            winner = combat(np1, np2)
        else:
            winner = 1 if c1 > c2 else 2
        # move cards
        if winner == 1:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
    return 1 if p1 else 2

combat(p1, p2)
wp = reversed(p1 if p1 else p2)
print(sum([(i + 1) * c for i, c in enumerate(wp)]))
