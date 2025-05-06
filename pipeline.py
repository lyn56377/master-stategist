# --- File: pipeline.py ---
from agent import AnalysisAgent
from solutions import SolutionsAgent
from what_to_do import WhatToDoAgent


def run_full_strategy(user_input: str):
    # 1) Analysis stage
    analysis_agent = AnalysisAgent(name="AnalysisAgent")
    response_text = analysis_agent.generate_response(user_input)

    # Parse analysis_data from the response text
    lines = response_text.splitlines()
    analysis_data = {'category': None, 'aspects': []}
    for line in lines:
        if line.startswith('- Category:'):
            analysis_data['category'] = line.split(':',1)[1].strip()
        if line.startswith('- Critical Aspects:'):
            analysis_data['aspects'] = [a.strip() for a in line.split(':',1)[1].split(',')]

    # Display the raw Analysis output
    print(response_text)

    # 2) Solutions stage
    solutions_agent = SolutionsAgent()
    solutions_data = solutions_agent.generate_policy(analysis_data)
    print("\n--- Solutions ---")
    print(solutions_data['policy'])

    # 3) What To Do stage
    what_agent = WhatToDoAgent()
    steps = what_agent.generate_actions(solutions_data)
    print("\n--- What To Do ---")
    for step in steps:
        print(f"* {step['action']} (When: {step['when']}, Why: {step['why']}, Where: {step.get('where','')}, Resources: {step.get('resources','')}, Effort: {step.get('effort','')})")


if __name__ == '__main__':
    user_input = input("Enter your personal challenge: ")
    run_full_strategy(user_input)
