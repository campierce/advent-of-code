import aocd
data = aocd.get_data(year=2020, day=23)

# O(len(cups) * moves)
# moves is small, so this is fine
# could reduce to O(moves) with linked list
# see part2 for that

cups = [int(x) for x in data]
HI = max(cups)

i = 0
for _ in range(100):
    # save trio
    pickup = [cups[(i+di+1)%HI] for di in range(3)]
    # pick dst
    dst = cups[i] - 1 if cups[i] > 1 else HI
    while dst in pickup:
        dst = dst - 1 if dst > 1 else HI
    # insert trio
    new = []
    for c in cups:
        if c in pickup:
            continue
        new.append(c)
        if c == dst:
            new.extend(pickup)
    # update i
    i = (new.index(cups[i]) + 1) % HI
    cups = new

i = cups.index(1)
print(''.join(str(cups[(i+di+1)%HI]) for di in range(HI-1)))
