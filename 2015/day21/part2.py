from itertools import combinations, product
from math import ceil
from aocd import get_data
data = get_data(year=2015, day=21)

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
ring_pairs = combinations(rings, 2)

def gear():
    for g in product(weapons, armor, ring_pairs):
        yield g

def get_stats(g, i):
    return (g[0][i] +
            g[1][i] +
            sum(map(lambda x: x[i], g[2])))

def player_wins(p1, boss):
    p1_dpt = max(p1[1] - boss[2], 1)
    boss_dpt = max(boss[1] - p1[2], 1)
    return ceil(boss[0]/p1_dpt) <= ceil(p1[0]/boss_dpt)

def main():
    # hp=0;damage=1;armor=2
    boss = [int(x.split()[-1]) for x in data.split('\n')]
    ans = float('-inf')
    for g in gear():
        p1 = [100, get_stats(g, 1), get_stats(g, 2)]
        if not player_wins(p1, boss):
            ans = max(ans, get_stats(g, 0))
    return ans

print(main())
