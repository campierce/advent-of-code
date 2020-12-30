import aocd
import itertools as it
import math
data = aocd.get_data(year=2015, day=24)

nums = [int(x) for x in data.split('\n')]
target = sum(nums) // 3
for r in range(1, len(nums)):
    combos = [x for x in it.combinations(nums, r) if sum(x) == target]
    if len(combos) > 0:
        break
print(min([math.prod(x) for x in combos]))
