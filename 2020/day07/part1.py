import aocd
import collections
import re
data = aocd.get_data(year=2020, day=7)

lines = [re.findall(r'(\w+ \w+) bag', x) for x in data.split('\n')]
graph = collections.defaultdict(list)
for line in lines:
    parent = line[0]
    for child in line[1:]:
        graph[child].append(parent)

ans = set()
stack = list(graph['shiny gold'])
while stack:
    child = stack.pop()
    if child not in ans:
        ans.add(child)
        for parent in graph[child]:
            stack.append(parent)
print(len(ans))
