import aocd
import collections
import itertools as it
data = aocd.get_data(year=2015, day=13)

lines = [x.split(' ') for x in data.split('\n')]
graph = collections.defaultdict(dict)
for line in lines:
    src = line[0]
    dst = line[-1][:-1]
    sign = 1 if line[2] == 'gain' else -1
    units = int(line[3])
    graph[src][dst] = sign * units

graph['me'] = {}
for k in graph.keys():
    if k != 'me':
        graph[k]['me'] = 0
        graph['me'][k] = 0

points = []
for p in it.permutations(graph.keys()):
    p2 = p + (p[0],)
    points.append(sum(graph[x][y] + graph[y][x] for x, y in zip(p2, p2[1:])))
print(max(points))
