class Stack:
    """Python implementation of a Stack Data Structure"""
    def __init__(self):
        '''Initializes the stack without any data'''
        self.items = []
    def isEmpty(self):
        '''Checks to see if there are items in the stack
           returns true or false'''
        return self.items ==[]
    def push(self, item):
        '''Adds an item to the top of the Stack'''
        self.items.append(item)
    def pop(self):
        '''Removes an item from the top of the Stack'''
        return self.items.pop()
    def peek(self):
        '''returns the first object at the top of the Stack'''
        return self.items[len(self.items)-1]
    def size(self):
        '''Retruns the length of the Stack'''
        return len(self.items)
