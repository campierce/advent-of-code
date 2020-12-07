from aocd import get_data
data = get_data(year=2015, day=18)

class Lights:

    def __init__(self, t0_state):
        self.rows = self.cols = len(t0_state)
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.temp = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.rows):
                self.grid[r][c] = 1 if t0_state[r][c] == '#' else 0

    def state(self, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols:
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

    def illuminate_corners(self):
        for r in (0, self.rows - 1):
            for c in (0, self.cols - 1):
                self.grid[r][c] = 1

    def animate(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.temp[r][c] = self.next_state(r, c)
        self.grid, self.temp = self.temp, self.grid

    def lit(self):
        return sum(map(sum, self.grid))

def main():
    lights = Lights(data.split('\n'))
    lights.illuminate_corners()
    for _ in range(100):
        lights.animate()
        lights.illuminate_corners()
    return lights.lit()

print(main())
