import re
from aocd import get_data
data = get_data(year=2020, day=7)

lines = [re.findall(r'(\d? ?\w+ \w+) bag', x) for x in data.split('\n')]
graph = {y[0]: [x.split(' ', 1) for x in y[1:]] for y in lines}

def bags_in(key):
    ans = 0
    for n, k in graph[key]:
        if k == 'no other':
            return ans
        ans += int(n)
        ans += int(n) * bags_in(k)
    return ans

print(bags_in('shiny gold'))
