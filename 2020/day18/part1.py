from aocd import get_data
data = get_data(year=2020, day=18)

mult = lambda x, y: x * y
addr = lambda x, y: x + y
def evaluate(stack):
    ans = 1
    op = mult
    while stack:
        ch = stack.pop()
        if ch == ')':
            return ans
        if ch == '(':
            ans = op(ans, evaluate(stack))
        elif ch == '+':
            op = addr
        elif ch == '*':
            op = mult
        else:
            ans = op(ans, int(ch))
    return ans

ans = 0
for line in data.split('\n'):
    stack = list(reversed(line.replace(' ', '')))
    ans += evaluate(stack)

print(ans)
