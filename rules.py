from rule_ast import Node

def create_rule(rule_string):
    # Simple mock parser for demo, replace with actual parsing logic
    if "age" in rule_string:
        return Node("operand", value={"attribute": "age", "operator": ">", "value": 30})
    return None

def combine_rules(rules):
    if len(rules) > 1:
        combined_ast = Node("operator", left=rules[0], right=rules[1], value="AND")
        return combined_ast
    return rules[0]

def evaluate_rule(ast, data):
    if ast.type == "operand":
        return eval(f"{data[ast.value['attribute']]} {ast.value['operator']} {ast.value['value']}")
    elif ast.type == "operator":
        left_eval = evaluate_rule(ast.left, data)
        right_eval = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_eval and right_eval
        elif ast.value == "OR":
            return left_eval or right_eval
