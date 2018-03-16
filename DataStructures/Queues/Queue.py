class Queue:
     """Python implementation of a Queue Data Structure."""
     def __init__(self):
        """Initializes an empty queue object."""
        self.items = []
     def isEmpty():
        """Returns a boolean value depending on whether the Queue has items(False)
        or does not(True)."""
        return self.items == []
     def enqueue(self, item):
        """Adds a new item to the back of the Queue using O(n)."""
        self.items.insert(0,item)
     def dequeue(self):
        """Removes the first item in the Queue and returns the item."""
        return self.items.pop()
     def size(self):
        """Returns the number of items in the Queue."""
        return len(self.items)