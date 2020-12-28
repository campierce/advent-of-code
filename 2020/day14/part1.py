import aocd
data = aocd.get_data(year=2020, day=14)

lines = data.split('\n')

mem = {}
zmask = omask = None
for line in lines:
    op, arg = line.split(' = ')
    if op == 'mask':
        zmask = int(arg.replace('X', '0'), 2)
        omask = int(arg.replace('X', '1'), 2)
    else:
        val = int(arg)
        val |= zmask
        val &= omask
        mem[op] = val

print(sum(mem.values()))
