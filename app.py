from flask import Flask, request, jsonify
from rules import create_rule, evaluate_rule
from database import save_rule, get_rule_by_id

app = Flask(__name__)

# Root route to show that the server is running
@app.route('/')
def index():
    return "Welcome to the Rule Engine API."

# Create rule route
@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule')
    ast = create_rule(rule_string)
    save_rule(rule_string, ast)
    return jsonify({"message": "Rule created and saved."})

# Evaluate rule route
@app.route('/evaluate', methods=['POST'])
def evaluate_rule_api():
    rule_id = request.json.get('rule_id')
    data = request.json.get('data')
    ast = get_rule_by_id(rule_id)
    result = evaluate_rule(ast, data)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
