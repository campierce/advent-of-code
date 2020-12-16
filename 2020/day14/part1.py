import re
from aocd import get_data
data = get_data(year=2020, day=14)

ans = {}
for x in data.split('mask = ')[1:]:
    mask = x[:36]
    for k, val in re.findall(r'\nmem\[(\d+)\] = (\d+)', x):
        val = int(val)
        sb = []
        for i in range(36):
            if mask[35-i] != 'X':
                sb.append(mask[35-i])
            else:
                if val & (1 << i):
                    sb.append('1')
                else:
                    sb.append('0')

        ans[k] = int(''.join(reversed(sb)), 2)

print(sum(ans.values()))
