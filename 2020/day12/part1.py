import aocd
data = aocd.get_data(year=2020, day=12)

i = x = y = 0
compass = ['E', 'S', 'W', 'N']

for line in data.split('\n'):
    op, val = line[0], int(line[1:])

    if op == 'L':
        i -= val // 90
    elif op == 'R':
        i += val // 90
    elif op == 'F':
        op = compass[i%4]

    if op == 'N':
        y += val
    elif op == 'S':
        y -= val
    elif op == 'E':
        x += val
    elif op == 'W':
        x -= val

print(abs(y) + abs(x))
