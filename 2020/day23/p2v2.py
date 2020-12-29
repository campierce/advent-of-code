import aocd
data = aocd.get_data(year=2020, day=23)

HI = 1000000
nums = [int(x) for x in data]
nums.extend(x for x in range(max(nums) + 1, HI + 1))
ll = [0] * (HI + 1)
for i, n in enumerate(nums):
    ll[nums[i-1]] = n

curr = nums[0]
for _ in range(10000000):
    t1 = ll[curr]
    t2 = ll[t1]
    t3 = ll[t2]
    ll[curr] = ll[t3]
    dst = curr - 1 if curr > 1 else HI
    while dst in (t1, t2, t3):
        dst = dst - 1 if dst > 1 else HI
    ll[t3] = ll[dst]
    ll[dst] = t1
    curr = ll[curr]

print(ll[1] * ll[ll[1]])
