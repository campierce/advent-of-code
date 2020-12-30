import aocd
import json
data = aocd.get_data(year=2015, day=12)

def explore(tree, nums):
    if isinstance(tree, int):
        nums.append(tree)
    elif isinstance(tree, list):
        for elem in tree:
            explore(elem, nums)
    elif isinstance(tree, dict):
        new_nums = []
        for k, v in tree.items():
            if v == 'red':
                new_nums.clear()
                break
            else:
                explore(v, new_nums)
        nums.append(sum(new_nums))

nums = []
tree = json.loads(data)
explore(tree, nums)
print(sum(nums))
