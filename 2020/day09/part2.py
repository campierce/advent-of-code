from itertools import combinations
from aocd import get_data
data = get_data(year=2020, day=9)

lines = [int(x) for x in data.split('\n')]

total = left = 0
for i, n in enumerate(lines):
    total += n
    while total > 36845998:
        total -= lines[left]
        left += 1
    if total == 36845998:
        arr = lines[left:i+1]
        print(min(arr) + max(arr))
        break
