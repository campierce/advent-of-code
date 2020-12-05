from aocd import get_data
data = get_data(year=2020, day=1)

nums = [int(x) for x in data.split('\n')]

def two_sum(target):
    seen = set()
    for n in nums:
        x = target - n
        if x in seen:
            return x * n
        seen.add(n)

print(two_sum(2020))
