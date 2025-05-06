# --- File: solutions.py ---
# Renamed GuidingPolicyAgent -> SolutionsAgent
class SolutionsAgent:
    """
    Generates a solutions outline from analysis data.
    """
    def __init__(self):
        self.name = "SolutionsAgent"

    def generate_policy(self, analysis_data: dict) -> dict:
        category = analysis_data.get('category')
        # Analogy-inspired personal strategy templates
        policy_templates = {
            'Financial Security': 'Track every dollar, seal leakages, and allocate income into priority buckets: needs, savings, wants.',
            'Productivity': 'Chunk major tasks into 15-minute focused sprints and reward completion to overcome procrastination.',
            'Relationship': 'Establish a communication protocol: listen fully first, then respond with empathy.',
            'Work-Life Balance': 'Define clear work vs. personal boundaries and enforce daily shutdown rituals.',
            'Health & Energy': 'Diagnose energy patterns like a clinical case: track symptoms and apply therapeutic routines to restore wellness.',
            'Negotiation': 'Frame difficult interactions as diplomatic negotiations: choose measured pressure or collaborative bargaining.',
            'Career Strategy': 'Treat your career as a competitive marketplace: identify a unique niche advantage and double-down on it.',
            'Habit Overhaul': 'Map and reorganize outdated routines by eliminating inefficiencies and instituting lean daily practices.',
            'Social Initiative': 'Use a feint-and-punch approach in social settings: start with low-stakes interactions, then take leadership roles.',
            'Unclassified': 'Clarify core issues and align resources toward primary objectives.'
        }
        policy = policy_templates.get(category, policy_templates['Unclassified'])
        return {
            'policy': policy,
            'category': category,
            'aspects': analysis_data.get('aspects', [])
        }
