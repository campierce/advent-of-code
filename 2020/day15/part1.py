from aocd import get_data
data = get_data(year=2020, day=15)

nums = [int(x) for x in data.split(',')]
seen = {nums[i]: i+1 for i in range(len(nums)-1)}

prev = nums[-1]
for i in range(len(nums)+1, 2021):
    if prev in seen:
        temp = prev
        prev = i - 1 - seen[prev]
        seen[temp] = i - 1
    else:
        seen[prev] = i - 1
        prev = 0
print(prev)
