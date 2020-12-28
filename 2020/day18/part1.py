import aocd
data = aocd.get_data(year=2020, day=18)

# realized after:
# simpler solution is to overload operators

mult = lambda x, y: x * y
addr = lambda x, y: x + y

def evaluate(stack):
    res, op = 1, mult
    while stack:
        ch = stack.pop()
        if ch == ')':
            return res
        if ch == '(':
            res = op(res, evaluate(stack))
        elif ch == '+':
            op = addr
        elif ch == '*':
            op = mult
        else:
            res = op(res, int(ch))
    return res

ans = 0
for line in data.split('\n'):
    stack = list(reversed(line.replace(' ', '')))
    ans += evaluate(stack)

print(ans)
