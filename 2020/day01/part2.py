from aocd import get_data
data = get_data(year=2020, day=1)

nums = [int(x) for x in data.split('\n')]

def three_sum(target):
    seen = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            x = target - nums[i] - nums[j]
            if x in seen:
                return x * nums[i] * nums[j]
        seen.add(nums[i])

print(three_sum(2020))
