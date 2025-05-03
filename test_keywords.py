# File: test_keywords.py

from pipeline import run_full_strategy

# A list of single keywords—each should trigger all 3 stages
keyword_inputs = [
    "budget",
    "deadline",
    "communication",
    "burnout",
    "fatigue",
    "negotiate",
    "skill gap",
    "routine",
    "introvert"
]

for kw in keyword_inputs:
    print("\n" + "="*50)
    print(f"🔑  Testing keyword: {kw!r}\n")
    
    # run_full_strategy should return a dict with keys: diagnosis, policy, actions
    result = run_full_strategy(kw)
    
    # 1) Diagnosis
    diag = result['diagnosis']
    print("🩺 Diagnosis")
    print(f"  • Challenge: {diag['challenge']!r}")
    print(f"  • Category: {diag['category']!r}")
    print(f"  • Aspects: {diag['aspects']}")
    print(f"  • Problems: {diag['problems']}")
    
    # 2) Guiding Policy
    print("\n📋 Guiding Policy")
    print(f"  {result['policy']['policy']}\n")
    
    # 3) Coherent Actions
    print("🚀 Coherent Actions")
    for step in result['actions']:
        print(f"  - {step['action']}")
        print(f"      When:     {step['when']}")
        print(f"      Why:      {step['why']}")
        print(f"      Where:    {step['where']}")
        print(f"      Resources:{step['resources']}")
        print(f"      Effort:   {step['effort']}\n")
