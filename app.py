# File: app.py

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Import your three agents + all needed helpers
from classifier import classify
from extractor import extract_aspects, extract_problems, prioritize_problems
from analogs import get_analogs
from knowledge_base import knowledge_base, problem_advice
from agent import AnalysisAgent
from solutions import SolutionsAgent
from what_to_do import WhatToDoAgent

app = Flask(
    __name__,
    template_folder='templates',  # your index.html lives in ./templates/
    static_folder='static'        # optional: serve images, CSS from ./static/
)
CORS(app)  # allow AJAX from any origin

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/strategy', methods=['POST'])
def strategy():
    data = request.get_json(force=True) or {}
    user_input = data.get('challenge', '').strip()

    # 1) Analysis stage (structured data)
    category    = classify(user_input)
    aspects     = extract_aspects(user_input, category)
    problems    = extract_problems(user_input)
    prioritized = prioritize_problems(problems)
    entry       = knowledge_base.get(category, {})

    analysis_data = {
        'challenge': user_input,
        'category': category,
        'description': entry.get('description', ''),
        'aspects': aspects,
        'problems': problems,
        'prioritized_problems': prioritized,
        'analogous_cases': entry.get('past_cases', []),
        'category_advice': entry.get('advice', '')
    }

    # 2) Solutions stage
    sol_agent      = SolutionsAgent()
    solutions_data = sol_agent.generate_policy(analysis_data)

    # 3) What To Do stage
    wtd_agent       = WhatToDoAgent()
    what_to_do_data = wtd_agent.generate_actions(solutions_data)

    # Bundle everything into one JSON response
    return jsonify({
        'analysis':   analysis_data,
        'solutions':  solutions_data,
        'what_to_do': what_to_do_data
    })

if __name__ == '__main__':
    # In development you can use debug=True for auto-reload and nicer errors
    app.run(host='0.0.0.0', port=5000, debug=True)
    # in app.py, below your existing `@app.route('/')`:

@app.route('/strategy', methods=['GET'])
def strategy_page():
    return render_template('strategy.html')
