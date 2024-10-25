from rules import create_rule, combine_rules, evaluate_rule

def test_create_rule():
    rule = "age > 30"
    ast = create_rule(rule)
    assert ast.type == "operand"
    assert ast.value["attribute"] == "age"

def test_combine_rules():
    rule1 = create_rule("age > 30")
    rule2 = create_rule("salary > 50000")
    combined_ast = combine_rules([rule1, rule2])
    assert combined_ast.type == "operator"
    assert combined_ast.value == "AND"

def test_evaluate_rule():
    rule = create_rule("age > 30")
    data = {"age": 35}
    result = evaluate_rule(rule, data)
    assert result == True

if __name__ == "__main__":
    test_create_rule()
    test_combine_rules()
    test_evaluate_rule()
    print("All tests passed!")
