from itertools import combinations
from math import prod
from aocd import get_data
data = get_data(year=2015, day=24)

nums = [int(x) for x in data.split('\n')]
target = sum(nums) // 4
for r in range(1, len(nums)):
    combos = [x for x in combinations(nums, r) if sum(x) == target]
    if len(combos) > 0:
        break
print(min([prod(x) for x in combos]))
