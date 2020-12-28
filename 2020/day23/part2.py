import aocd
data = aocd.get_data(year=2020, day=23)

class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = self.right = None

HI = 1000000
nums = [int(x) for x in data]
nums.extend([x for x in range(max(nums) + 1, 1000001)])
nodes = [None for _ in range(HI + 1)]
curr = Node()
for n in nums:
    curr.right = Node(n)
    curr.right.left = curr
    nodes[n] = curr.right
    curr = curr.right
head = nodes[nums[0]]
head.left = curr
curr.right = head
curr = head

for _ in range(10000000):
    # extract trio
    trio = curr.right
    pickup = set([trio.val, trio.right.val, trio.right.right.val])
    curr.right = curr.right.right.right.right
    curr.right.left = curr
    # pick dst
    label = curr.val - 1 if curr.val > 1 else HI
    while label in pickup:
        label = label - 1 if label > 1 else HI
    dst = nodes[label]
    # insert trio
    temp = dst.right
    dst.right = trio
    trio.left = dst
    trio.right.right.right = temp
    temp.left = trio.right.right
    # update curr
    curr = curr.right

print(nodes[1].right.val * nodes[1].right.right.val)
