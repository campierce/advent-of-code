import aocd
import itertools as it
import math
data = aocd.get_data(year=2015, day=21)

weapons = [[8, 4, 0]
    ,[10, 5, 0]
    ,[25, 6, 0]
    ,[40, 7, 0]
    ,[74, 8, 0]]
armor = [[0, 0, 0]
    ,[13, 0, 1]
    ,[31, 0, 2]
    ,[53, 0, 3]
    ,[75, 0, 4]
    ,[102, 0, 5]]
rings = [[0, 0, 0]
    ,[0, 0, 0]
    ,[25, 1, 0]
    ,[50, 2, 0]
    ,[100, 3, 0]
    ,[20, 0, 1]
    ,[40, 0, 2]
    ,[80, 0, 3]]
ring_pairs = it.combinations(rings, 2)

def gear():
    for g in it.product(weapons, armor, ring_pairs):
        yield g

def stat(g, i):
    # g: ([cost, damage, armor], ...)
    return (g[0][i] +
            g[1][i] +
            sum([x[i] for x in g[2]]))

def p1_wins(p1, ai):
    p1_dpt = max(p1[1] - ai[2], 1)
    ai_dpt = max(ai[1] - p1[2], 1)
    return math.ceil(ai[0] / p1_dpt) <= math.ceil(p1[0] / ai_dpt)

def main():
    # ai/p1: [hp, damage, armor]
    ai = [int(x.split()[-1]) for x in data.split('\n')]
    ans = float('inf')
    for g in gear():
        p1 = [100, stat(g, 1), stat(g, 2)]
        if p1_wins(p1, ai):
            ans = min(ans, stat(g, 0))
    return ans

print(main())
