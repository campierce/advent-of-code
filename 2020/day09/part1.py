import aocd
import itertools as it
data = aocd.get_data(year=2020, day=9)

PRE = 25
nums = [int(x) for x in data.split('\n')]

for i in range(PRE, len(nums)):
    seen = set([x + y for x, y in it.combinations(nums[i-PRE:i], 2)])
    if nums[i] not in seen:
        print(nums[i])
        break
