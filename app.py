import gradio as gr
import pickle
from environment import TrafficEnv
from agent import QAgent

# Load trained model
agent = QAgent()
try:
    with open("q_table.pkl", "rb") as f:
        agent.q_table = pickle.load(f)
except:
    pass

env = TrafficEnv()

def run_simulation(steps=10):
    state = env.reset()
    output = ""

    for step in range(steps):
        action = agent.choose_action(state)
        next_state, reward, _ = env.step(action)

        output += f"""
Step {step}
🚗 North: {state[0]} | South: {state[1]}
🚦 Signal: {'NS Green' if state[2]==0 else 'EW Green'}
👉 Action: {'Switch' if action==1 else 'Keep'}
⭐ Reward: {reward}
----------------------
"""
        state = next_state

    return output

gr.Interface(
    fn=run_simulation,
    inputs=gr.Slider(5, 50, step=5, label="Steps"),
    outputs="text",
    title="🚦 Traffic Signal AI (RL)"
).launch()