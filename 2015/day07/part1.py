from functools import cache
from aocd import get_data
data = get_data(year=2015, day=7)

@cache
def get_signal(dst):
    if dst not in sources:
        return int(dst)
    src = sources[dst]
    if len(src) == 1:
        return get_signal(src[0])
    if len(src) == 2:
        return ~ get_signal(src[-1])
    else:
        sig1 = get_signal(src[0])
        sig2 = get_signal(src[2])
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
print(get_signal('a'))
