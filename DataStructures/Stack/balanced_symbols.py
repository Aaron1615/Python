import Stack

def check_parenthesis(my_string):
    """This function checks for matched Paranthesis, Square Bracekts, and curly braces
    when given an input string(my_string). Returns true if they match otherwise
    retruns false"""
    my_stack = Stack.Stack()
    for piece in my_string:
        if piece in "([{":
            my_stack.push(piece)
        elif piece in ")]}":
            first = my_stack.pop()
            if not matches(first,piece):
                return False
    return my_stack.isEmpty()

def matches(open,close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)
            

#Test Cases
print(check_parenthesis('{asdfad{([asdfasd]afsdad3[])}(asdfas)}'))
print(check_parenthesis('[{()]'))      
print(check_parenthesis("()()()()()()("))
        