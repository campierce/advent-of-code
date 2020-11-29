from collections import defaultdict
from aocd import get_data
data = get_data(year=2015, day=13)

lines = [x.split(' ') for x in data.split('\n')]
pairs = defaultdict(dict)
for line in lines:
    src = line[0]
    nbr = line[-1][:-1]
    sign = 1 if line[2] == 'gain' else -1
    units = int(line[3])
    pairs[src][nbr] = sign * units

def optimize_seats():
    src = state[-1]
    if len(state) == len(pairs):
        nbr = state[0]
        return pairs[src][nbr] + pairs[nbr][src]
    score = float('-inf')
    for nbr, units in pairs[src].items():
        if nbr not in state:
            state.append(nbr)
            score = max(score, units + pairs[nbr][src] + optimize_seats())
            state.pop()
    return score

state = [lines[0][0]]
ans = optimize_seats()
print(ans)
