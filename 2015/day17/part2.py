import aocd
data = aocd.get_data(year=2015, day=17)

def dfs(v=0, i=0, n=0):
    if v == 150:
        containers.append(n)
        return
    if v > 150 or i == len(nums):
        return
    dfs(v + nums[i], i + 1, n + 1)
    dfs(v, i + 1, n)

nums = [int(x) for x in data.split('\n')]
containers = []
dfs()
print(containers.count(min(containers)))
