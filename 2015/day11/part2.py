from aocd import get_data
data = get_data(year=2015, day=11)

def is_straight(seq, start, end):
    for i in range(start, end):
        if seq[i] != chr(ord(seq[i+1]) - 1):
            return False
    return True

def is_valid(seq):
    has_straight = False
    paired = set()
    for i, char in enumerate(seq):
        if i >= 2 and not has_straight:
            has_straight = is_straight(seq, i-2, i)
        if char in ('i', 'o', 'l'):
            return False
        if i >= 1 and char == seq[i-1]:
            paired.add(char)
    return has_straight and len(paired) >= 2

def increment(seq):
    seq.reverse()
    for i, char in enumerate(seq):
        if char == 'z':
            seq[i] = 'a'
        else:
            seq[i] = chr(ord(char) + 1)
            break
    seq.reverse()

def get_new_pw(old_pw):
    seq = list(old_pw)
    while True:
        increment(seq)
        if is_valid(seq):
            break
    return ''.join(seq)

part1 = get_new_pw(data)
print(get_new_pw(part1))
