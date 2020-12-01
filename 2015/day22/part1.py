from aocd import get_data
data = get_data(year=2015, day=22)

def is_prunable(state):
    return (state['spent'] >= ans or
            state['p1'] <= 0 or
            state['mana'] < 53)

def magic_missile(state):
    temp = state.copy()
    temp['mana'] -= 53
    temp['spent'] += 53
    temp['ai'] -= 4
    dfs(temp)

def drain(state):
    temp = state.copy()
    temp['mana'] -= 73
    temp['spent'] += 73
    temp['ai'] -= 2
    temp['p1'] += 2
    dfs(temp)

def shield(state):
    temp = state.copy()
    temp['mana'] -= 113
    temp['spent'] += 113
    temp['shield'] += 6
    dfs(temp)

def poison(state):
    temp = state.copy()
    temp['mana'] -= 173
    temp['spent'] += 173
    temp['poison'] += 6
    dfs(temp)

def recharge(state):
    temp = state.copy()
    temp['mana'] -= 229
    temp['spent'] += 229
    temp['recharge'] += 5
    dfs(temp)

def update_ans(state):
    global ans
    ans = min(ans, state['spent'])

def run_effects(state):
    state['turn'] = not state['turn']
    if state['shield'] > 0:
        state['shield'] -= 1
    if state['poison'] > 0:
        state['poison'] -= 1
        state['ai'] -= 3
    if state['recharge'] > 0:
        state['recharge'] -= 1
        state['mana'] += 101

def run_ai_turn(state):
    run_effects(state)
    if state['ai'] <= 0:
        update_ans(state)
        return
    armor = 7 if state['shield'] > 0 else 0
    state['p1'] -= max(1, state['damage'] - armor)
    dfs(state)

def run_p1_turn(state):
    run_effects(state)
    if is_prunable(state):
        return
    if state['ai'] <= 0:
        update_ans(state)
        return
    magic_missile(state)
    if state['mana'] >= 73:
        drain(state)
    if state['mana'] >= 113 and state['shield'] == 0:
        shield(state)
    if state['mana'] >= 173 and state['poison'] == 0:
        poison(state)
    if state['mana'] >= 229 and state['recharge'] == 0:
        recharge(state)

def dfs(state):
    if state['turn']:
        run_p1_turn(state)
    else:
        run_ai_turn(state)

ans = float('inf')
t0_state = {'turn': True,
    'p1': 50,
    'mana': 500,
    'spent': 0,
    'shield': 0,
    'poison': 0,
    'recharge': 0}
props = [int(x.split()[-1]) for x in data.split('\n')]
t0_state['ai'] = props[0]
t0_state['damage'] = props[1]
dfs(t0_state)
print(ans)
