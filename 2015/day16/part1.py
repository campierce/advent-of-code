import aocd
data = aocd.get_data(year=2015, day=16)

temp = data.replace(':', '').replace(',', '')
lines = [x.split(' ') for x in temp.split('\n')]

ref = {('children', '3')
    ,('cats', '7')
    ,('samoyeds', '2')
    ,('pomeranians', '3')
    ,('akitas', '0')
    ,('vizslas', '0')
    ,('goldfish', '5')
    ,('trees', '3')
    ,('cars', '2')
    ,('perfumes', '1')}

def setify(arr):
    ht = set()
    for i in range(2, len(arr), 2):
        ht.add((arr[i], arr[i+1]))
    return ht

for line in lines:
    if setify(line).issubset(ref):
        print(line[1])
        break
