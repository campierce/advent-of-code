import aocd
data = aocd.get_data(year=2015, day=15)

lines = [x.split(' ') for x in data.replace(',', '').split('\n')]
props = [[int(x[i]) for i in range(2, 11, 2)] for x in lines]

def permutations(length, total):
    if length == 1:
        yield (total,)
    else:
        for n in range(total + 1):
            for permu in permutations(length - 1, total - n):
                yield (n,) + permu

def score(permu):
    cals = [props[i][4] * permu[i] for i in range(4)]
    if sum(cals) != 500:
        return float('-inf')
    score = 1
    for j in range(4):
        prop = [props[i][j] * permu[i] for i in range(4)]
        score *= max(sum(prop), 0)
    return score

ans = float('-inf')
for permu in permutations(4, 100):
    ans = max(ans, score(permu))
print(ans)
