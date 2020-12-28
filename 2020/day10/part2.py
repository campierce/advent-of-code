import aocd
import functools as ft
data = aocd.get_data(year=2020, day=10)

nums = [int(x) for x in data.split('\n')]
nums.append(0)
nums.sort()

@ft.cache
def ways_to_connect_from(i):
    if i == len(nums) - 1:
        return 1
    ans = 0
    for j in range(i+1, min(i+4, len(nums))):
        if nums[j] - nums[i] <= 3:
            ans += ways_to_connect_from(j)
    return ans

print(ways_to_connect_from(0))
