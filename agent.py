import random

class QAgent:
    def __init__(self):
        self.q_table = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice([0, 1])
        q0 = self.get_q(state, 0)
        q1 = self.get_q(state, 1)
        return 0 if q0 > q1 else 1

    def update(self, state, action, reward, next_state):
        old_q = self.get_q(state, action)
        future_q = max(self.get_q(next_state, 0), self.get_q(next_state, 1))

        new_q = old_q + self.alpha * (reward + self.gamma * future_q - old_q)
        self.q_table[(state, action)] = new_q