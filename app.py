# File: app.py

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Import your three agents + all needed helpers
from classifier import classify
from extractor import extract_aspects, extract_problems, prioritize_problems
from analogs import get_analogs
from knowledge_base import knowledge_base, problem_advice
from agent import DiagnosisAgent
from guiding_policy import GuidingPolicyAgent
from coherent_actions import CoherentActionsAgent

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

    # 1) Diagnosis stage (structured data)
    category   = classify(user_input)
    aspects    = extract_aspects(user_input, category)
    problems   = extract_problems(user_input)
    prioritized= prioritize_problems(problems)
    entry      = knowledge_base.get(category, {})

    diagnosis_data = {
        'challenge': user_input,
        'category': category,
        'description': entry.get('description', ''),
        'aspects': aspects,
        'problems': problems,
        'prioritized_problems': prioritized,
        'analogous_cases': entry.get('past_cases', []),
        'category_advice': entry.get('advice', '')
    }

    # 2) Guiding policy stage
    gp_agent   = GuidingPolicyAgent()
    policy_data= gp_agent.generate_policy(diagnosis_data)

    # 3) Coherent actions stage
    ca_agent   = CoherentActionsAgent()
    actions_data = ca_agent.generate_actions(policy_data)

    # Bundle everything into one JSON response
    return jsonify({
        'diagnosis': diagnosis_data,
        'policy':    policy_data,
        'actions':   actions_data
    })

if __name__ == '__main__':
    # In development you can use debug=True for auto-reload and nicer errors
    app.run(host='0.0.0.0', port=5000, debug=True)
