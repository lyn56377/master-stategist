
# --- File: agent.py ---
# A minimal base class instead of external dependency
class AssistantAgent:
    def __init__(self, name: str):
        self.name = name
    def generate_response(self, user_input: str) -> str:
        raise NotImplementedError

from classifier import classify
from extractor import extract_aspects, extract_problems, prioritize_problems
from analogs import get_analogs
from knowledge_base import knowledge_base, problem_advice

class DiagnosisAgent(AssistantAgent):
    def generate_response(self, user_input: str) -> str:
        category = classify(user_input)
        aspects = extract_aspects(user_input, category)
        problems = extract_problems(user_input)
        prioritized = prioritize_problems(problems)
        entry = knowledge_base.get(category, {})
        description = entry.get("description", "No description available.")
        cases = entry.get("past_cases", [])
        advice = entry.get("advice", "Consider specialized resources.")

        # Build core response
        response = [
            f"Diagnosis:",
            f"- Challenge: {user_input}",
            f"- Category: {category}",
            f"- Description: {description}",
            f"- Critical Aspects: {', '.join(aspects) or 'None detected'}"
        ]
        # Prioritized problems
        if prioritized:
            response.append("- Identified Problems (with Priority):")
            for p, score in prioritized:
                response.append(f"  * {p} (Priority {score})")
        else:
            response.append("- Identified Problems: None detected")
        # Analogous cases
        if cases:
            response.append("- Analogous Cases:")
            for c in cases:
                response.append(f"  * {c}")
        else:
            response.append("- Analogous Cases: None found.")
        # Category advice
        response.append(f"- Strategic Advice based on Category: {advice}")
        # Problem-specific advice
        problem_advices = [problem_advice.get(p) for p, _ in prioritized]
        problem_advices = [pa for pa in problem_advices if pa]
        if problem_advices:
            response.append("- Additional Advice based on Specific Problems:")
            for pa in problem_advices:
                response.append(f"  * {pa}")

        return "\n".join(response)
