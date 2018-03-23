from node import Node

class ordered_list:
    """Implementation of the ordered List data structure.
    Each item in the list is sorted in ascending order"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Returns True if the list is empty, else returns False"""
        return self.head == None

    def size(self):
        """Returns the length of the list"""
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.get_next()
            
        return count

    def remove(self,item):
        """Removes the item from the list"""
        current = self.head
        previous = None
        while current.get_data() != item:
            previous = current
            current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def search(self, item):
        """Searches for the item in the list returning True if it is there
        otherwise returning False"""
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_next() == item:
                found = True
            else:
                if current.get_data() < item:
                    stop = True
                else:
                    current = current.get_next()

        return found       

    def add(self,item):
        """Adds an item to the list returning the list order"""
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        new_node = Node(item)
        if previous != None:
            new_node.set_next(current)
            previous.set_next(new_node)
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def index(self, item):
        """Returns the index of the item"""
        index = 0
        current = self.head
        while current != item:
            current = current.get_next()
            index += 1
        return index
    
    def pop(self,position=None):
        """Removes and returns the item at position, assuming position
        is the end if no value is given"""
        current = self.head
        previous = None
        index = 0
        while (position != None and index != position) or (position == None and current.get_next() != None):
            index += 1
            previous = current
            current = current.get_next()
        if previous != None:
            previous.set_next(current.get_next())
        else:
            current = None            
   