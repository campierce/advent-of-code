from aocd import get_data
data = get_data(year=2015, day=14)

lines = [x.split(' ') for x in data.split('\n')]
racers = {x[0]:
            {'speed': int(x[3])
            ,'move': int(x[6])
            ,'rest': int(x[13])}
        for x in lines}

ans = float('-inf')
for k, v in racers.items():
    time = 2503
    dist = 0
    is_resting = False
    while time > 0:
        if not is_resting:
            temp = min(v['move'], time)
            dist += v['speed'] * temp
            time -= temp
        else:
            temp = min(v['rest'], time)
            time -= temp
        is_resting = not is_resting
    ans = max(ans, dist)
print(ans)
