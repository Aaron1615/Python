import Stack

def base_converter(decimal_number, base):
    """Converts a base 10 number(decimal_number) into a different base(base)
    number between 1 and 16."""
    
    values = "0123456789ABCDEF"
    store = Stack.Stack()
    while decimal_number > 0:
        remainder = decimal_number%base
        store.push(remainder)
        decimal_number = decimal_number //base
    output = ""
    while not store.isEmpty():
        output= output + str(values[store.pop()])
    return output
