from binary_tree import binary_tree
from Stack import Stack

def build_parse_tree(expression):
    """Takes a parenthetical expression string and 
    converts it into a tree with operands as leaves
    and all non leaf nodes as operators.
    
    This function requires the Stack and binary_tree
    data structure implementations.
    """
    exp_list = expression.split()
    tree_stack = Stack()
    tree = binary_tree('')
    tree_stack.push(tree)
    current_tree = tree

    for i in exp_list:
        
        if i =="(":
            current_tree.insert_left('')
            tree_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i in ['+','-','/','*']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            tree_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ")":
                current_tree = tree_stack.pop()
        else:
            try:
                current_tree.set_root_val(int(i))
                parent = tree_stack.pop()
                current_tree = parent
            except ValueError:
                raise ValueError("Token '{}' is not a valid integer".format(i))
    return tree

def evaluate_tree(tree):
    """Returns the result of evaluating the expression
    in the tree."""
    left = tree.get_left_child()
    right = tree.get_right_child()

    if left and right:
        func = tree.get_root_val()
        if func == "+":
            return evaluate_tree(left) + evaluate_tree(right)
        elif func == "-":
            return evaluate_tree(left) - evaluate_tree(right)
        elif func == "*":
            return evaluate_tree(left) * evaluate_tree(right)
        elif func == "/":
            return evaluate_tree(left) / evaluate_tree(right)
    else:
        return tree.get_root_val()
pt = build_parse_tree("( ( 10 + 5 ) * 3 )")

def post_order_eval(tree):
    """Uses postorder transversal to evaluate the tree."""
    left = None
    right= None
    if tree:
        left = post_order_eval(tree.get_left_child())
        right = post_order_eval(tree.get_right_child())
        if left and right:
            func = tree.get_root_val()
            if func == "+":
                return left + right
            elif func == "-":
                return left - right
            elif func == "*":
                return left * right
            elif func == "/":
                return left / right
        else:
            return tree.get_root_val()

def print_expression(tree):
    """Returns the parenthetical notation of the tree."""
    expression = ""
    if tree.get_left_child() and tree.get_right_child():
        expression += " (" + str(print_expression(tree.get_left_child()))
        expression += str(tree.get_root_val())
        expression += str(print_expression(tree.get_right_child())) + ") "
        return expression
    else:
        return " " + str(tree.get_root_val()) + " "