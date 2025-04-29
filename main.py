# --- File: main.py ---
from agent import DiagnosisAgent

def main():
    agent = DiagnosisAgent(name="MasterStrategistAgent")
    print("=== Master Strategist Diagnosis ===")
    while True:
        text = input("Enter your personal problem (or 'exit'): ")
        if text.lower() in ('exit', 'quit'):
            break
        print(agent.generate_response(text))

if __name__ == "__main__":
    main()
