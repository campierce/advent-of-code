from aocd import get_data
data = get_data(year=2020, day=8)

lines = [(x[0], int(x[1])) for x in [y.split() for y in data.split('\n')]]

pc = acc = 0
seen = set()
while pc not in seen:
    seen.add(pc)
    op, val = lines[pc]
    if op == 'acc':
        acc += val
        pc += 1
    elif op == 'jmp':
        pc += val
    else:
        pc += 1
print(acc)
