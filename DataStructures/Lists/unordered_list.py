from node import Node
class Unordered_list:
    """implementation of an unordered list data structure in Python"""
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """Returns True if empty, otherwise returns false"""
        return self.head ==None

    def add(self, item):
        """Adds the item to the front of the list"""
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """Returns the size of the list"""
        current = self.head
        count = 0
        while current != None:
            count +=1
            current = current.get_next()
        return count

    def search(self,item):
        """Returns True if the item is present, otherwise
        returns false"""
        current = self.head
        found = False
        while not found and current != None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    
    def remove(self,item):
        """Removes item from the list"""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def append(self,item):
        """Adds an item to the end of the list"""
        current = self.head
        previous = None
        if self.head != None:
            while current != None:
                previous = current
                current = current.get_next()
            previous.set_next(Node(item))
        else:
            self.head= Node(item)

    def insert(self,item,index):
        """Adds an item to at the given index of the list"""
        previous = None
        current = self.head
        position = 0
        if index != 0:
            while position != index:
                previous = current
                current = current.get_next()
                position += 1
            previous.set_next(Node(item))
            previous.get_next().set_next(current)
        else:
            self.add(item)

    def index(self,item):
        """Returns the index of the requested item"""
        current = self.head
        position = 0
        while current != None:
            if current.get_data() == item:
               return position
            else:
                current = current.get_next()
                position += 1

    def pop(self,item = None):
        """Removes the last item from the list and returns it"""
        current =self.head
        previous = None
        stop= False
        while not stop:
            if current.get_data() == item or (item == None and current.get_next() == None):
                stop = True
            else:
                previous = current
                current= current.get_next()
        if previous != None:
            previous.set_next(current.get_next())
        elif current.get_next() == None:
            self.head = None
        else:
            self.head = current.get_next()

        return current.get_data()
