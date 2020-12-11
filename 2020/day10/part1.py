from aocd import get_data
data = get_data(year=2020, day=10)

nums = [int(x) for x in data.split('\n')]
nums.sort()

prev = d1 = 0
d3 = 1
for n in nums:
    diff = n - prev
    if diff == 1:
        d1 += 1
    elif diff == 3:
        d3 += 1
    prev = n

print(d1 * d3)
