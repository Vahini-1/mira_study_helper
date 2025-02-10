from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


MIRA_API_KEY = "sb-a318e89b2c2e683026b2d2787c4e7d30"


MIRA_FLOW_URLS = {
    "essay": "https://flows.mira.network/flows?author=vahini&flow=essay-checker",
    "debugger": "https://flows.mira.network/flows?author=vahini&flow=code-debugger",
    "qa": "https://flows.mira.network/flows?author=vahini&flow=qna-generator",
    "concepts": "https://flows.mira.network/flows?author=vahini&flow=concept-explainer"
}

headers = {
    "Authorization": f"Bearer {MIRA_API_KEY}",
    "Content-Type": "application/json"
}

# Endpoint 1: Essay Checker
@app.route('/essay', methods=['POST'])
def essay_checker():
    data = request.json
    response = requests.post(MIRA_FLOW_URLS["essay"], json={"task": "essay", "input": data["text"]}, headers=headers)
    return jsonify(response.json())

# Endpoint 2: Coding Debugger & Explainer
@app.route('/debugger', methods=['POST'])
def coding_debugger():
    data = request.json
    response = requests.post(MIRA_FLOW_URLS["debugger"], json={"task": "debugger", "input": data["code"]}, headers=headers)
    return jsonify(response.json())


# Endpoint 3: Q&A Generator
@app.route('/qa', methods=['POST'])
def qa_generator():
    data = request.json
    response = requests.post(MIRA_FLOW_URLS["qa"], json={"task": "qa", "input": data["questions"]}, headers=headers)
    return jsonify(response.json())

# Endpoint 4: Concept Explainer
@app.route('/concepts', methods=['POST'])
def concept_explainer():
    data = request.json
    response = requests.post(MIRA_FLOW_URLS["concepts"], json={"task": "concepts", "input": data["subject"]}, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

