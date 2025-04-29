
# --- File: extractor.py ---
from rules import rules

# Extract critical aspects based on category keywords
def extract_aspects(text: str, category: str) -> list[str]:
    t = text.lower()
    return [kw for kw in rules.get(category, []) if kw in t]

# Identify problem keywords in user input
def extract_problems(text: str) -> list[str]:
    problem_keywords = [
        'burnout','overwork','stress','anxiety','conflict','loneliness',
        'communication issue','trust issue','deadline pressure',
        'family problem','relationship problem','friendship issue','career uncertainty'
    ]
    t = text.lower()
    return [kw for kw in problem_keywords if kw in t]

# Priority scoring for problems
problem_priority = {
    'burnout': 10,
    'overwork': 9,
    'stress': 8,
    'anxiety': 7,
    'conflict': 6,
    'trust issue': 5,
    'communication issue': 5,
    'deadline pressure': 4,
    'loneliness': 4,
    'family problem': 3,
    'relationship problem': 3,
    'friendship issue': 2,
    'career uncertainty': 1
}

def prioritize_problems(problems: list[str]) -> list[tuple[str,int]]:
    scored = [(p, problem_priority.get(p, 0)) for p in problems]
    return sorted(scored, key=lambda x: x[1], reverse=True)
