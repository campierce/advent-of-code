import aocd
import itertools as it
data = aocd.get_data(year=2020, day=13)

lines = data.split('\n')
nums = [(i, int(x)) for i, x in enumerate(lines[1].split(',')) if x != 'x']

ans = nums[0][1]
step = 1
for offset, bus in nums:
    for time in it.count(ans, step):
        if (time + offset) % bus == 0:
            ans = time
            break
    step *= bus
print(ans)
