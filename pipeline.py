# --- File: pipeline.py ---
from agent import DiagnosisAgent
from guiding_policy import GuidingPolicyAgent
from coherent_actions import CoherentActionsAgent


def run_full_strategy(user_input: str):
    # 1) Diagnose
    diag_agent = DiagnosisAgent(name="DiagnosisAgent")
    # Assuming DiagnosisAgent has a method to return raw data dict
    # We'll extract diagnosis_data by calling a method or parsing generate_response
    # For this pipeline, let's assume generate_data returns the dict
    try:
        # If you implemented a dedicated method
        diagnosis_data = diag_agent.diagnose_data(user_input)
    except AttributeError:
        # Fallback: parse from generate_response output if no dedicated method
        # Here, we'll simulate by reconstructing a dict
        response_text = diag_agent.generate_response(user_input)
        # Simple parser example (customize as needed)
        lines = response_text.splitlines()
        diagnosis_data = { 'category': None, 'aspects': [] }
        for line in lines:
            if line.startswith('- Category:'):
                diagnosis_data['category'] = line.split(':',1)[1].strip()
            if line.startswith('- Critical Aspects:'):
                diagnosis_data['aspects'] = [a.strip() for a in line.split(':',1)[1].split(',')]

    # Print diagnosis response
    print(response_text)

    # 2) Guiding Policy
    gp_agent = GuidingPolicyAgent()
    policy_data = gp_agent.generate_policy(diagnosis_data)
    print("\n--- Guiding Policy ---")
    print(policy_data['policy'])

    # 3) Coherent Actions
    ca_agent = CoherentActionsAgent()
    actions = ca_agent.generate_actions(policy_data)
    print("\n--- Coherent Actions ---")
    for step in actions:
        print(f"* {step['action']} (When: {step['when']}, Why: {step['why']}, Where: {step['where']}, Resources: {step['resources']}, Effort: {step['effort']})")


if __name__ == '__main__':
    user_input = input("Enter your personal challenge: ")
    run_full_strategy(user_input)

