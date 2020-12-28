from collections import Counter
from itertools import chain
from aocd import get_data
data = get_data(year=2020, day=21)

cnt = Counter()
couldbe = {}
for line in data.split('\n'):
    x, y = line.split(' (contains ')
    ingredients = x.split()
    allergens = y[:-1].split(', ')
    cnt.update(ingredients)
    for a in allergens:
        if a not in couldbe:
            couldbe[a] = set(ingredients)
        else:
            couldbe[a] &= set(ingredients)

unsafe = set(chain.from_iterable(couldbe.values()))
print(sum(v for k, v in cnt.items() if k not in unsafe))
