import re
from collections import defaultdict, Counter
from aocd import get_data
data = get_data(year=2020, day=7)

lines = [re.findall(r'(\w+ \w+) bag', x) for x in data.split('\n')]
graph = defaultdict(list)
for line in lines:
    parent = line[0]
    for child in line[1:]:
        graph[child].append(parent)

ans = set()
stack = list(graph['shiny gold'])
while stack:
    child = stack.pop()
    ans.add(child)
    stack += graph[child]
print(len(ans))
