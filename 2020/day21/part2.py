import aocd
data = aocd.get_data(year=2020, day=21)

couldbe = {}
for line in data.split('\n'):
    x, y = line.split(' (contains ')
    ingredients = x.split()
    allergens = y[:-1].split(', ')
    for a in allergens:
        if a not in couldbe:
            couldbe[a] = set(ingredients)
        else:
            couldbe[a] &= set(ingredients)

pairs = []
used = set()
while len(pairs) < len(couldbe):
    for a, iset in couldbe.items():
        opt = iset - used
        if len(opt) == 1:
            i = min(opt)
            pairs.append((a, i))
            used.add(i)

print(','.join(x[1] for x in sorted(pairs)))
