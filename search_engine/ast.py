import ast
class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  
        self.value = value  
        self.left = left  
        self.right = right 


import re

def create_rule(rule_string):
    tokens = re.findall(r"[\w']+|[()><=]", rule_string)
    stack = []
    
    for token in tokens:
        if token.isdigit():
            stack.append(Node("operand", int(token)))
        elif re.match(r"[><=]", token):
            right = stack.pop()
            left = stack.pop()
            stack.append(Node("operator", token, left, right))
        elif token == "AND" or token == "OR":
            right = stack.pop()
            left = stack.pop()
            stack.append(Node("operator", token, left, right))
        elif re.match(r"[\w']+", token):
            stack.append(Node("operand", token))
    
    return stack[0]

def combine_rules(rules):
    combined_ast = None
    for rule_string in rules:
        rule_ast = create_rule(rule_string)
        if combined_ast is None:
            combined_ast = rule_ast
        else:
            combined_ast = Node("operator", "AND", combined_ast, rule_ast)
    
    return combined_ast

def evaluate_rule(ast, data):
    if ast.type == "operand":
        return data.get(ast.value, None)
    elif ast.type == "operator":
        left_val = evaluate_rule(ast.left, data)
        right_val = evaluate_rule(ast.right, data)
        if ast.value == ">":
            return left_val > right_val
        elif ast.value == "<":
            return left_val < right_val
        elif ast.value == "=":
            return left_val == right_val
        elif ast.value == "AND":
            return left_val and right_val
        elif ast.value == "OR":
            return left_val or right_val

