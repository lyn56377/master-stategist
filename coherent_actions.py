
# --- File: coherent_actions.py ---
class CoherentActionsAgent:
    """
    Generates a set of coherent coordinated actions from a guiding policy.
    """
    def __init__(self):
        self.name = "CoherentActionsAgent"

    def generate_actions(self, policy_data: dict) -> list[dict]:
        policy = policy_data.get('policy', '')
        # Personal strategy action templates inspired by analogies
        action_templates = {
            # Financial Security actions
            'Track every dollar, seal leakages, and allocate income into priority buckets: needs, savings, wants.': [
                {
                    'action': 'Log today’s expenses',
                    'when': 'Tonight',
                    'why': 'Increase spending visibility',
                    'where': 'Budgeting app or spreadsheet',
                    'resources': 'Budgeting tool',
                    'effort': '10 minutes'
                },
                {
                    'action': 'Automate 50/30/20 split on payday',
                    'when': 'Each payday',
                    'why': 'Enforce disciplined savings',
                    'where': 'Online banking portal',
                    'resources': 'Bank settings',
                    'effort': '15 minutes'
                },
                {
                    'action': 'Weekly budget review session',
                    'when': 'Sunday evenings',
                    'why': 'Identify overspending and adjust',
                    'where': 'Home office',
                    'resources': 'Spreadsheet or app',
                    'effort': '20 minutes'
                }
            ],
            # Productivity actions
            'Chunk major tasks into 15-minute focused sprints and reward completion to overcome procrastination.': [
                {
                    'action': 'List top 3 tasks and break into micro-steps',
                    'when': 'Tomorrow morning',
                    'why': 'Reduce overwhelm and start momentum',
                    'where': 'Planner or note app',
                    'resources': 'Notebook',
                    'effort': '10 minutes'
                },
                {
                    'action': 'Run 15-minute Pomodoro sprint',
                    'when': 'Hourly during workday',
                    'why': 'Maintain high focus and energy',
                    'where': 'Desk area',
                    'resources': 'Timer app',
                    'effort': '15 minutes per sprint'
                },
                {
                    'action': 'Record completed sprints and feelings',
                    'when': 'End of day',
                    'why': 'Track progress and adjust strategies',
                    'where': 'Journal',
                    'resources': 'Journal or app',
                    'effort': '5 minutes'
                }
            ],
            # Relationship actions
            'Establish a communication protocol: listen fully first, then respond with empathy.': [
                {
                    'action': 'Implement no-interrupt rule in conversation',
                    'when': 'Next discussion',
                    'why': 'Ensure each person feels heard',
                    'where': 'Living room or dinner table',
                    'resources': 'Timer',
                    'effort': '2 minutes'
                },
                {
                    'action': 'Use I-statements to share feelings',
                    'when': 'Mid-week',
                    'why': 'Reduce blame and defensiveness',
                    'where': 'Private talk',
                    'resources': 'Conversation guide',
                    'effort': '10 minutes each'
                },
                {
                    'action': 'Schedule a positive joint activity',
                    'when': 'Weekend',
                    'why': 'Build positive experiences',
                    'where': 'Local event or home',
                    'resources': 'Calendar invite',
                    'effort': '1 hour'
                }
            ],
            # Work-Life Balance actions
            'Define clear work vs. personal boundaries and enforce daily shutdown rituals.': [
                {
                    'action': 'Block 7–9pm as personal time',
                    'when': 'Daily after work',
                    'why': 'Protect personal downtime',
                    'where': 'Digital calendar',
                    'resources': 'Calendar app',
                    'effort': '5 minutes'
                },
                {
                    'action': 'Write down 3 self-care activities each morning',
                    'when': 'Every morning',
                    'why': 'Prioritize personal well-being',
                    'where': 'Planner',
                    'resources': 'Notebook',
                    'effort': '3 minutes'
                },
                {
                    'action': 'Conduct weekly shutdown ritual',
                    'when': 'Friday evening',
                    'why': 'Mentally close work week',
                    'where': 'Workspace',
                    'resources': 'Checklist',
                    'effort': '15 minutes'
                }
            ],
            # Health & Energy actions
            'Diagnose energy patterns like a clinical case: track symptoms and apply therapeutic routines to restore wellness.': [
                {
                    'action': 'Track sleep and mood daily',
                    'when': 'Every morning',
                    'why': 'Identify fatigue triggers',
                    'where': 'Sleep-tracker app',
                    'resources': 'Smartphone',
                    'effort': '5 minutes'
                },
                {
                    'action': 'Plan weekly meal with balanced nutrients',
                    'when': 'Weekly',
                    'why': 'Ensure dietary support for energy',
                    'where': 'Kitchen',
                    'resources': 'Meal plan template',
                    'effort': '30 minutes'
                },
                {
                    'action': 'Schedule light exercise sessions',
                    'when': '3 times a week',
                    'why': 'Boost stamina and mood',
                    'where': 'Local park or gym',
                    'resources': 'Workout gear',
                    'effort': '20 minutes each'
                }
            ],
            # Negotiation actions
            'Frame difficult interactions as diplomatic negotiations: choose measured pressure or collaborative bargaining.': [
                {
                    'action': 'Assess counterpart style (firm vs. flexible)',
                    'when': 'Before next conversation',
                    'why': 'Tailor negotiation approach',
                    'where': 'Reflection notebook',
                    'resources': 'Notebook',
                    'effort': '10 minutes'
                },
                {
                    'action': 'Draft concession offers and counterpoints',
                    'when': 'Day of negotiation',
                    'why': 'Prepare bargaining leverage',
                    'where': 'Workspace',
                    'resources': 'Note cards',
                    'effort': '20 minutes'
                },
                {
                    'action': 'Hold a structured negotiation meeting',
                    'when': 'Scheduled session',
                    'why': 'Ensure clear rules and progress',
                    'where': 'Neutral location',
                    'resources': 'Agenda, timer',
                    'effort': '1 hour'
                }
            ],
            # Career Strategy actions
            'Treat your career as a competitive marketplace: identify a unique niche advantage and double-down on it.': [
                {
                    'action': 'Map personal skills vs. market demand',
                    'when': 'This week',
                    'why': 'Spot high-value areas',
                    'where': 'Online research',
                    'resources': 'Industry reports',
                    'effort': '1 hour'
                },
                {
                    'action': 'Enroll in targeted skill course',
                    'when': 'Next month',
                    'why': 'Build niche expertise',
                    'where': 'E-learning platform',
                    'resources': 'Course subscription',
                    'effort': '5 hours/week'
                },
                {
                    'action': 'Apply new skills in a side project',
                    'when': 'Within 2 weeks of course start',
                    'why': 'Reinforce learning with practice',
                    'where': 'Personal lab',
                    'resources': 'Project outline',
                    'effort': '2 hours'
                }
            ],
            # Habit Overhaul actions
            'Map and reorganize outdated routines by eliminating inefficiencies and instituting lean daily practices.': [
                {
                    'action': 'Write down current daily routine step-by-step',
                    'when': 'Tomorrow morning',
                    'why': 'Identify bottlenecks',
                    'where': 'Journal',
                    'resources': 'Notebook',
                    'effort': '15 minutes'
                },
                {
                    'action': 'Eliminate two low-value steps (e.g. social media scroll)',
                    'when': 'The following day',
                    'why': 'Free time for high-impact tasks',
                    'where': 'Personal schedule',
                    'resources': 'Calendar app',
                    'effort': '5 minutes'
                },
                {
                    'action': 'Implement one new productive habit',
                    'when': 'Start of next week',
                    'why': 'Replace removed steps with value',
                    'where': 'Workspace or home',
                    'resources': 'Habit-tracker app',
                    'effort': '10 minutes/day'
                }
            ],
            # Social Initiative actions
            'Use a feint-and-punch approach in social settings: start with low-stakes interactions, then take leadership roles.': [
                {
                    'action': 'Attend a casual meetup event',
                    'when': 'Next available meet',
                    'why': 'Low-stakes social feint',
                    'where': 'Local community',
                    'resources': 'Event listing',
                    'effort': '1 hour'
                },
                {
                    'action': 'Introduce self and ask open-ended questions',
                    'when': 'During meetup',
                    'why': 'Practice social engagement',
                    'where': 'Event venue',
                    'resources': 'Conversation starters',
                    'effort': '5 minutes'
                },
                {
                    'action': 'Organize a small group activity',
                    'when': 'Within 3 weeks',
                    'why': 'Punch—lead a social initiative',
                    'where': 'Chosen venue',
                    'resources': 'Group invite',
                    'effort': '2 hours'
                }
            ]
        }
        return action_templates.get(policy, [])
