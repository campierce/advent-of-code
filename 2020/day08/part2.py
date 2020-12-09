from aocd import get_data
data = get_data(year=2020, day=8)

lines = [x.split() for x in data.split('\n')]

def boot():
    pc = acc = 0
    seen = set()
    while pc < len(lines):
        if pc in seen:
            return None
        seen.add(pc)
        op, val = lines[pc]
        if op == 'acc':
            acc += int(val)
            pc += 1
        elif op == 'jmp':
            pc += int(val)
        else:
            pc += 1
    return acc

swap = {'jmp': 'nop', 'nop': 'jmp'}
for line in lines:
    if line[0] == 'acc':
        continue
    line[0] = swap[line[0]]
    ans = boot()
    if ans is not None:
        print(ans)
        break
    line[0] = swap[line[0]]
