import aocd
data = aocd.get_data(year=2020, day=1)

nums = [int(x) for x in data.split('\n')]

seen = set()
for n in nums:
    x = 2020 - n
    if x in seen:
        print(x * n)
        break
    seen.add(n)
