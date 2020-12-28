import aocd
import re
data = aocd.get_data(year=2020, day=16)

valid = set()
temp = re.findall(r'[a-z ]+: (\d+)-(\d+) or (\d+)-(\d+)', data)
for x1, y1, x2, y2 in [map(int, x) for x in temp]:
    valid.update(list(range(x1, y1+1)), list(range(x2, y2+1)))

temp = data.split('nearby tickets:\n')[1]
nums = [int(x) for x in re.split(r',|\n', temp)]

ans = 0
for n in nums:
    if n not in valid:
        ans += n
print(ans)
