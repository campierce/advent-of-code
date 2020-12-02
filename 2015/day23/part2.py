from aocd import get_data
data = get_data(year=2015, day=23)

lines = [x for x in data.split('\n')]
regs = {'a': 1, 'b': 0}
i = 0
while i < len(lines):
    instr, r = lines[i].split(' ', 1)
    di = 1
    if instr == 'hlf':
        regs[r] //= 2
    elif instr == 'tpl':
        regs[r] *= 3
    elif instr == 'inc':
        regs[r] += 1
    elif instr == 'jmp':
        di = int(r)
    elif instr == 'jie':
        r, offset = r.split(',')
        if regs[r] % 2 == 0:
            di = int(offset)
    elif instr == 'jio':
        r, offset = r.split(',')
        if regs[r] == 1:
            di = int(offset)
    i += di
print(regs['b'])
