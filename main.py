
# --- File: main.py ---
from agent import AnalysisAgent

def main():
    agent = AnalysisAgent(name="MasterStrategistAgent")
    print("=== Master Strategist Analysis ===")
    while True:
        text = input("Enter your personal problem (or 'exit'): ")
        if text.lower() in ('exit', 'quit'):
            break
        print(agent.generate_response(text))

if __name__ == "__main__":
    main()