from aocd import get_data
data = get_data(year=2020, day=15)

nums = [int(x) for x in data.split(',')]
seen = {n: i+1 for i, n in enumerate(nums)}
prev = nums[-1]
del seen[prev]

for i in range(len(nums), 2020):
    if prev not in seen:
        seen[prev] = i
    temp = prev
    prev = i - seen[prev]
    seen[temp] = i

print(prev)
