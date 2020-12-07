from aocd import get_data
data = get_data(year=2015, day=20)

target = int(data)
arr = [0 for _ in range(target // 10)]
for i in range(1, target // 10):
    for j in range(i, min(i * 51, target // 10), i):
        arr[j] += i * 11
for i, n in enumerate(arr):
    if n >= target:
        print(i)
        break
