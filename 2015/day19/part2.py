from aocd import get_data
data = get_data(year=2015, day=19)

lines = data.split('\n')
molecule = lines[-1]
reduction = {x[1]: x[0] for x in [x.split(' => ') for x in lines[:-2]]}
reducables = sorted(reduction.keys(), reverse=True, key=len)

def collapse(s):
    if s == 'e':
        return 0
    for r in reducables:
        if r in s:
            return 1 + collapse(s.replace(r, reduction[r], 1))

print(collapse(molecule))
