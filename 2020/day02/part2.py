from aocd import get_data
data = get_data(year=2020, day=2)

lines = [x.split(' ', 1) for x in data.split('\n')]
ans = 0
for line in lines:
    lo, hi = [int(x) - 1 for x in line[0].split('-')]
    char, pw = line[1].split(': ')
    if (pw[lo] == char) ^ (pw[hi] == char):
        ans += 1
print(ans)
