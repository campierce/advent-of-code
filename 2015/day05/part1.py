from aocd import get_data
data = get_data(year=2015, day=5)

lines = data.split('\n')
vowels = set(['a', 'e', 'i', 'o', 'u'])
illegal = set(['ab', 'cd', 'pq', 'xy'])
ans = 0
for line in lines:
    vowel_cnt = 0
    has_aa = False
    is_legal = True
    prev = ''
    for char in line:
        if char in vowels:
            vowel_cnt += 1
        if char == prev:
            has_aa = True
        if prev + char in illegal:
            is_legal = False
            break
        prev = char
    if vowel_cnt >= 3 and has_aa and is_legal:
        ans += 1
print(ans)
