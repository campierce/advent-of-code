from aocd import get_data
data = get_data(year=2015, day=14)

lines = [x.split(' ') for x in data.split('\n')]

ans = float('-inf')
for x in lines:
    speed, move, rest = int(x[3]), int(x[6]), int(x[13])
    q, r = divmod(2503, move + rest)
    dist = (q * move + min(r, move)) * speed
    ans = max(ans, dist)
print(ans)
