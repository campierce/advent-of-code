from aocd import get_data
data = get_data(year=2015, day=18)

class Lights:

    def __init__(self, t0_state):
        self.grid = [[0 for _ in range(100)] for _ in range(100)]
        self.temp = [[0 for _ in range(100)] for _ in range(100)]
        for r in range(100):
            for c in range(100):
                self.grid[r][c] = 1 if t0_state[r][c] == '#' else 0

    def state(self, r, c):
        if 0 <= r < 100 and 0 <= c < 100:
            return self.grid[r][c]
        return 0

    def lit_neighbors(self, r, c):
        n = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if not dr == dc == 0:
                    n += self.state(r + dr, c + dc)
        return n

    def next_state(self, r, c):
        n = self.lit_neighbors(r, c)
        if self.grid[r][c] == 1:
            if n in (2, 3):
                return 1
            return 0
        else:
            if n == 3:
                return 1
            return 0

    def animate(self):
        for r in range(100):
            for c in range(100):
                self.temp[r][c] = self.next_state(r, c)
        self.grid, self.temp = self.temp, self.grid

def main():
    lights = Lights(data.split('\n'))
    for _ in range(100):
        lights.animate()
    return sum(map(sum, lights.grid))

print(main())
