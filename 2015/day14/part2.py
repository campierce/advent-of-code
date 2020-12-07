from aocd import get_data
data = get_data(year=2015, day=14)

speed, move, rest = [], [], []
lines = [x.split(' ') for x in data.split('\n')]
for x in lines:
    speed.append(int(x[3]))
    move.append(int(x[6]))
    rest.append(int(x[13]))

n = len(lines)
dist = [0] * n
points = [0] * n
for sec in range(2503):
    for i in range(n):
        if sec % (move[i] + rest[i]) < move[i]:
            dist[i] += speed[i]
    hi = max(dist)
    for i in range(n):
        if dist[i] == hi:
            points[i] += 1
print(max(points))
