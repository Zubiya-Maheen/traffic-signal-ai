import random

class TrafficEnv:
    def __init__(self):
        self.max_cars = 20
        self.reset()

    def reset(self):
        self.north = random.randint(0, 10)
        self.south = random.randint(0, 10)
        self.signal = 0  # 0 = NS green, 1 = EW green
        return self.get_state()

    def get_state(self):
        return (min(self.north, 10), min(self.south, 10), self.signal)

    def step(self, action):
        if action == 1:
            self.signal = 1 - self.signal

        # cars pass
        if self.signal == 0:
            self.north = max(0, self.north - 3)
            self.south = max(0, self.south - 3)

        # new cars arrive
        self.north += random.randint(0, 3)
        self.south += random.randint(0, 3)

        # reward
        waiting_penalty = -(self.north + self.south)
        switch_penalty = -2 if action == 1 else 0
        reward = waiting_penalty + switch_penalty

        done = False

        return self.get_state(), reward, done