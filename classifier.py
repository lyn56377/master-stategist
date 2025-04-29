
# --- File: classifier.py ---
import re
from rules import rules

def classify(text: str) -> str:
    t = text.lower()
    for cat, keywords in rules.items():
        for kw in keywords:
            if re.search(rf"\b{re.escape(kw)}\b", t):
                return cat
    return "Unclassified"
