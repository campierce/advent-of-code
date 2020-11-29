from aocd import get_data
data = get_data(year=2015, day=17)

def dfs(v=0, i=0):
    if v == 150:
        return 1
    if v > 150 or i == len(nums):
        return 0
    return dfs(v + nums[i], i + 1) + dfs(v, i + 1)

nums = [int(x) for x in data.split('\n')]
print(dfs())
