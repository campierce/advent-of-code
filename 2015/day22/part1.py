import aocd
import functools as ft
data = aocd.get_data(year=2015, day=22)

@ft.cache
def play(turn, hp, mana, op, shd, psn, chg):
    if hp <= 0:
        return float('inf')
    armor = 0
    if shd > 0:
        armor = 7
        shd -= 1
    if psn > 0:
        op -= 3
        psn -=1
    if chg > 0:
        mana += 101
        chg -= 1
    if op <= 0:
        return 0
    if not turn:
        hp -= max(1, dmg - armor)
        return play(not turn, hp, mana, op, shd, psn, chg)
    else:
        if hp <= 0 or mana < 53:
            return float('inf')
        turn = not turn
        lo = float('inf')
        lo = min(lo, 53+play(turn, hp, mana-53, op-4, shd, psn, chg))
        if mana >= 73:
            lo = min(lo, 73+play(turn, hp+2, mana-73, op-2, shd, psn, chg))
        if mana >= 113 and shd == 0:
            lo = min(lo, 113+play(turn, hp, mana-113, op, 6, psn, chg))
        if mana >= 173 and psn == 0:
            lo = min(lo, 173+play(turn, hp, mana-173, op, shd, 6, chg))
        if mana >= 229 and chg == 0:
            lo = min(lo, 229+play(turn, hp, mana-229 ,op, shd, psn, 5))
        return lo

props = [int(x.split()[-1]) for x in data.split('\n')]
dmg = props[1]
print(play(True, 50, 500, props[0], 0, 0, 0))
