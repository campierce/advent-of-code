import aocd
import collections
import itertools as it
data = aocd.get_data(year=2015, day=9)

lines = data.split('\n')
graph = collections.defaultdict(dict)
for line in lines:
    src, _, dst, _, dist = line.split()
    graph[src][dst] = int(dist)
    graph[dst][src] = int(dist)

distances = []
for p in it.permutations(graph.keys()):
    distances.append(sum(graph[x][y] for x, y in zip(p, p[1:])))
print(max(distances))
