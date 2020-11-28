from aocd import get_data
data = get_data(year=2015, day=5)

lines = data.split('\n')
ans = 0
for line in lines:
    seen = {}
    has_2aa = has_aba = False
    prevprev = prev = ''
    for i, char in enumerate(line):
        if char == prevprev:
            has_aba = True
        double = prev + char
        if double in seen:
            if seen[double] != i-1:
                has_2aa = True
        else:
            seen[prev+char] = i
        prevprev, prev = prev, char
        if has_2aa and has_aba:
            ans += 1
            break
print(ans)
