from aocd import get_data
data = get_data(year=2015, day=14)

class Racer:

    def __init__(self, speed, move, rest):
        self.km_per_second = speed
        self.move_time = move
        self.rest_time = rest
        self.is_resting = False
        self.time_until_switch = move
        self.distance = 0
        self.points = 0

    def check_for_switch(self):
        if self.time_until_switch == 0:
            if self.is_resting:
                self.time_until_switch = self.move_time
            else:
                self.time_until_switch = self.rest_time
            self.is_resting = not self.is_resting

    def pass_one_second(self):
        self.check_for_switch()
        if not self.is_resting:
            self.distance += self.km_per_second
        self.time_until_switch -= 1

    def receive_award(self):
        self.points += 1

lines = [x.split(' ') for x in data.split('\n')]
racers = [Racer(int(x[3]), int(x[6]), int(x[13])) for x in lines]
for i in range(2503):
    hi = float('-inf')
    for r in racers:
        r.pass_one_second()
        hi = max(hi, r.distance)
    for r in racers:
        if r.distance == hi:
            r.receive_award()

print(max(map(lambda x: x.points, racers)))
