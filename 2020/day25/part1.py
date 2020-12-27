from aocd import get_data
data = get_data(year=2020, day=25)

pk1, pk2 = [int(x) for x in data.split('\n')]

def transform(sn, ls):
    return pow(sn, ls, 20201227)

ls = 0
while transform(7, ls) != pk1:
    ls += 1

print(transform(pk2, ls))
