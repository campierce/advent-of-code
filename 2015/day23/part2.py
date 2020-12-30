import aocd
data = aocd.get_data(year=2015, day=23)

lines = [x for x in data.split('\n')]
regs = {'a': 1, 'b': 0}
i = 0
while i < len(lines):
    op, arg = lines[i].split(' ', 1)
    di = 1
    if op == 'hlf':
        regs[arg] //= 2
    elif op == 'tpl':
        regs[arg] *= 3
    elif op == 'inc':
        regs[arg] += 1
    elif op == 'jmp':
        di = int(arg)
    elif op == 'jie':
        r, offset = arg.split(',')
        if regs[r] % 2 == 0:
            di = int(offset)
    elif op == 'jio':
        r, offset = arg.split(',')
        if regs[r] == 1:
            di = int(offset)
    i += di
print(regs['b'])
