import aocd
data = aocd.get_data(year=2020, day=13)

lines = data.split('\n')
time = int(lines[0])
nums = [int(x) for x in lines[1].split(',') if x != 'x']

bus, wait = None, float('inf')
for n in nums:
    temp = n - (time % n)
    if temp < wait:
        wait = temp
        bus = n

print(bus * wait)
