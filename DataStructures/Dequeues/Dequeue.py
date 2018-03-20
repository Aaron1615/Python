class Dequeue:
    """Python implementation of a Dequeue Data Structure."""
    def __init__(self):
        self.items = []
    def add_front(self, item):
        """Adds an item to the back of the Dequeue"""
        self.items.append(item)
    def add_back(self,item):
        """Adds an item to the back of the Dequeue"""
        self.items.insert(0,item)
    def remove_front(self):
        return self.items.pop()
        """Removes an item from the front of the Dequeue and returns it"""
    def remove_back(self):
        return self.items.pop(0)
        """Removes an item from the back of the Dequeue and returns it"""
    def is_empty(self):
        return self.items == []
        """Returns a boolean value depending on whether the Dequeue has items(False)
        or does not(True)."""
    def size(self):
        """Returns the number of items in the Dequeue"""
        return len(self.items)
