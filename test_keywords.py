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
    
    result = run_full_strategy(kw)
    
    # 1) Analysis
    analysis = result['analysis']
    print("🩺 Analysis")
    print(f"  • Challenge: {analysis['challenge']!r}")
    print(f"  • Category: {analysis['category']!r}")
    print(f"  • Aspects: {analysis['aspects']}")
    print(f"  • Problems: {analysis['problems']}")
    
    # 2) Solutions
    print("\n📋 Solutions")
    print(f"  {result['solutions']['policy']}\n")
    
    # 3) What To Do
    print("🚀 What To Do")
    for step in result['what_to_do']:
        print(f"  - {step['action']}")
        print(f"      When:     {step['when']}")
        print(f"      Why:      {step['why']}")
        if 'where' in step:
            print(f"      Where:    {step['where']}")
        if 'resources' in step:
            print(f"      Resources:{step['resources']}")
        if 'effort' in step:
            print(f"      Effort:   {step['effort']}\n")
