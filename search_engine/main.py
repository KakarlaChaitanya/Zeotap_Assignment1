
from flask import Flask, request, jsonify
from ast import Node, create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

# Define the API endpoints

# 1. Create Rule endpoint
@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule')
    rule_ast = create_rule(rule_string)
    return jsonify({"message": "Rule created", "ast": str(rule_ast)})

# 2. Combine Rules endpoint
@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json.get('rules')
    combined_ast = combine_rules(rules)
    return jsonify({"message": "Rules combined", "ast": str(combined_ast)})

# 3. Evaluate Rule endpoint
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    ast = request.json.get('ast')
    data = request.json.get('data')
    result = evaluate_rule(ast, data)
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
