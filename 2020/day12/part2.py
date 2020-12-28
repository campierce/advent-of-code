import aocd
data = aocd.get_data(year=2020, day=12)

x = y = 0
wx, wy = 10, 1

for line in data.split('\n'):
    op, val = line[0], int(line[1:])

    if op == 'L':
        val = 360 - val
        op = 'R'

    if op == 'R':
        while val:
            wx, wy = wy, -wx
            val -= 90
    elif op == 'F':
        y += wy * val
        x += wx * val
    elif op == 'N':
        wy += val
    elif op == 'S':
        wy -= val
    elif op == 'E':
        wx += val
    elif op == 'W':
        wx -= val

print(abs(y) + abs(x))
