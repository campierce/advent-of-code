from itertools import combinations
from aocd import get_data
data = get_data(year=2020, day=9)

P1 = 36845998
nums = [int(x) for x in data.split('\n')]

def find_weakness():
    total = left = 0
    for i, n in enumerate(nums):
        total += n
        while total > P1:
            total -= nums[left]
            left += 1
        if total == P1:
            subarr = nums[left:i+1]
            return min(subarr) + max(subarr)

print(find_weakness())
