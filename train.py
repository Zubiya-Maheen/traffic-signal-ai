from environment import TrafficEnv
from agent import QAgent

env = TrafficEnv()
agent = QAgent()

episodes = 500

for ep in range(episodes):
    state = env.reset()

    for step in range(50):
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)

        agent.update(state, action, reward, next_state)
        state = next_state

print("Training complete!")

# Save model
import pickle
with open("q_table.pkl", "wb") as f:
    pickle.dump(agent.q_table, f)