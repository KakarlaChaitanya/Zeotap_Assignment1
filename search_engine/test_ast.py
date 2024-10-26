import pytest
from ast import Node, create_rule, combine_rules, evaluate_rule

# Test create_rule function
def test_create_rule():
    # Define a sample rule
    rule_string = "(age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')"
    # Create the AST from the rule
    ast = create_rule(rule_string)

    # Verify the AST structure
    assert ast is not None
    assert ast.type == "operator"
    assert ast.value == "OR"

    # Check left branch (age > 30 AND department = 'Sales')
    left_branch = ast.left
    assert left_branch.type == "operator"
    assert left_branch.value == "AND"
    assert left_branch.left.type == "operand"
    assert left_branch.left.value == "age > 30"
    assert left_branch.right.type == "operand"
    assert left_branch.right.value == "department = 'Sales'"

    # Check right branch (age < 25 AND department = 'Marketing')
    right_branch = ast.right
    assert right_branch.type == "operator"
    assert right_branch.value == "AND"
    assert right_branch.left.type == "operand"
    assert right_branch.left.value == "age < 25"
    assert right_branch.right.type == "operand"
    assert right_branch.right.value == "department = 'Marketing'"

# Test combine_rules function
def test_combine_rules():
    # Define multiple rule strings
    rule_string1 = "(age > 30 AND department = 'Sales')"
    rule_string2 = "(salary > 50000 OR experience > 5)"
    
    # Combine the rules
    combined_ast = combine_rules([rule_string1, rule_string2])
    
    # Verify the structure of the combined AST
    assert combined_ast is not None
    assert combined_ast.type == "operator"
    assert combined_ast.value == "AND"
    
    # Check left part of combined AST
    assert combined_ast.left.type == "operator"
    assert combined_ast.left.value == "AND"
    assert combined_ast.left.left.value == "age > 30"
    assert combined_ast.left.right.value == "department = 'Sales'"

    # Check right part of combined AST
    assert combined_ast.right.type == "operator"
    assert combined_ast.right.value == "OR"
    assert combined_ast.right.left.value == "salary > 50000"
    assert combined_ast.right.right.value == "experience > 5"

# Test evaluate_rule function
def test_evaluate_rule():
    rule_string = "(age > 30 AND department = 'Sales') OR (salary > 50000)"
    ast = create_rule(rule_string)
    
    data1 = {"age": 35, "department": "Sales", "salary": 40000, "experience": 3}
    data2 = {"age": 24, "department": "Marketing", "salary": 60000, "experience": 4}
    data3 = {"age": 28, "department": "Sales", "salary": 30000, "experience": 6}

    assert evaluate_rule(ast, data1) == True  
    assert evaluate_rule(ast, data2) == True  
    assert evaluate_rule(ast, data3) == False  
