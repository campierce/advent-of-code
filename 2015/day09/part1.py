from collections import defaultdict
from aocd import get_data
data = get_data(year=2015, day=9)

lines = [x.split(' ') for x in data.split('\n')]
distances = defaultdict(dict)
for line in lines:
    loc1 = line[0]
    loc2 = line[2]
    dist = int(line[4])
    distances[loc1][loc2] = dist
    distances[loc2][loc1] = dist

def min_dist_to_visit_all(src):
    if len(visited) + 1 == len(distances):
        return 0
    path = float('inf')
    visited.add(src)
    for dst, step in distances[src].items():
        if dst not in visited:
            path = min(path, step + min_dist_to_visit_all(dst))
    visited.remove(src)
    return path

visited = set()
ans = float('inf')
for src in distances.keys():
    ans = min(ans, min_dist_to_visit_all(src))
print(ans)
