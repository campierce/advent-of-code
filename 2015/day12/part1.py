import aocd
import json
data = aocd.get_data(year=2015, day=12)

def explore(tree):
    if isinstance(tree, int):
        nums.append(tree)
    elif isinstance(tree, list):
        for elem in tree:
            explore(elem)
    elif isinstance(tree, dict):
        for k, v in tree.items():
            explore(v)

nums = []
tree = json.loads(data)
explore(tree)
print(sum(nums))
