import Stack

def reverse_string(mystr):
    """Returns the reverse of the input string(mystr)"""
    my_stack = Stack.Stack()
    for letter in mystr:
        my_stack.push(letter)
    new_string = ""
    while not my_stack.isEmpty():
        new_string = new_string + my_stack.pop()
    return new_string
