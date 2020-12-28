import aocd
data = aocd.get_data(year=2020, day=14)

lines = data.split('\n')

def collapse(addr):
    if 'X' not in addr:
        yield int(addr, 2)
    else:
        yield from collapse(addr.replace('X', '0', 1))
        yield from collapse(addr.replace('X', '1', 1))

mask = None
mem = {}
for line in lines:
    op, arg = line.split(' = ')
    if op == 'mask':
        mask = arg
    else:
        temp = str(bin(int(op[4:-1])))[2:].rjust(36, '0')
        addr = ''.join([t if m == '0' else m for (m, t) in zip(mask, temp)])
        for permu in collapse(addr):
            mem[permu] = int(arg)

print(sum(mem.values()))
