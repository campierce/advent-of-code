from aocd import get_data
data = get_data(year=2020, day=1)

nums = [int(x) for x in data.split('\n')]
seen = set()
for i, n1 in enumerate(nums):
    for n2 in nums[i+1:]:
        x = 2020 - n1 - n2
        if x in seen:
            print(x * n1 * n2)
            break
    seen.add(n1)
