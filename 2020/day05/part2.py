from aocd import get_data
data = get_data(year=2020, day=5)

lines = [x for x in data.split('\n')]

def bspartition(s, start, end, lo_key):
    lo, hi = 0, 2 ** (end + 1 - start) - 1
    for i in range(start, end + 1):
        mid = (lo + hi) // 2
        if s[i] == lo_key:
            hi = mid
        else:
            lo = mid
    return hi

filled = set()
for line in lines:
    row = bspartition(line, 0, 6, 'F')
    col = bspartition(line, 7, 9, 'L')
    seat = row * 8 + col
    filled.add(seat)

valid = {x for x in range(min(filled), max(filled) + 1)}
for x in valid.difference(filled):
    print(x)
