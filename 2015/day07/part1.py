import aocd
import functools as ft
data = aocd.get_data(year=2015, day=7)

@ft.cache
def signal(dst):
    if dst not in sources:
        return int(dst)
    src = sources[dst]
    if len(src) == 1:
        return signal(src[0])
    if len(src) == 2:
        return ~ signal(src[-1])
    else:
        sig1 = signal(src[0])
        sig2 = signal(src[2])
        op = src[1]
        if op == 'AND':
            return sig1 & sig2
        elif op == 'OR':
            return sig1 | sig2
        elif op == 'LSHIFT':
            return sig1 << sig2
        else:
            return sig1 >> sig2

lines = [x.split() for x in data.split('\n')]
sources = {x[-1]: x[:-2] for x in lines}
print(signal('a'))
