import Stack

def decimal_to_binary(number):
    """Converts a base 10 number(number) into a binary number"""
    
    store = Stack.Stack()
    while number > 0:
        remainder = number%2
        store.push(remainder)
        number = number //2
    output = ""
    while not store.isEmpty():
        output= output + str(store.pop())
    return output
 