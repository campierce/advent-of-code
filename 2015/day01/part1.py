import aocd
data = aocd.get_data(year=2015, day=1)

moves = {'(': 1, ')': -1}
ans = 0
for char in data:
    ans += moves[char]
print(ans)
