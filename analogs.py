
# --- File: analogs.py ---
from knowledge_base import knowledge_base

def get_analogs(category: str) -> list[str]:
    entry = knowledge_base.get(category)
    # Return the past cases if the category exists, else an empty list
    return entry.get("past_cases", []) if entry else []
