from aocd import get_data
data = get_data(year=2015, day=1)

move = {'(': 1, ')': -1}
ans = 0
for i, char in enumerate(data):
    ans += move[char]
    if ans < 0:
        print(i+1)
        break
