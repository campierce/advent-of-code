from aocd import get_data
data = get_data(year=2015, day=16)

temp = data.replace(':', '').replace(',', '')
lines = [x.split(' ') for x in temp.split('\n')]

ref = {'children': 3
    ,'cats': 7
    ,'samoyeds': 2
    ,'pomeranians': 3
    ,'akitas': 0
    ,'vizslas': 0
    ,'goldfish': 5
    ,'trees': 3
    ,'cars': 2
    ,'perfumes': 1}

def dictify(arr):
    ht = {}
    for i in range(2, len(arr), 2):
        ht[arr[i]] = int(arr[i+1])
    return ht

def is_modified_subset(chk):
    for k, v in chk.items():
        if k in ('cats', 'trees'):
            if v <= ref[k]:
                return False
        elif k in ('pomeranians', 'goldfish'):
            if v >= ref[k]:
                return False
        elif v != ref[k]:
            return False
    return True

for line in lines:
    chk = dictify(line)
    if is_modified_subset(chk):
        print(line[1])
        break
