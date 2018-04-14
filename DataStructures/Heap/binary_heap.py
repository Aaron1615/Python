class min_binary_heap:
    """Implementation of a binary heap, a heap data structure
    in the form of a bianry tee in which all levels except
    the deepest are filled (shape property) and each key is less than or
    equal to the keys of it's children (heap property)."""
    def __init__(self):
        """Initializes a heap of size zero."""
        self.heap_list = [0]
        self.current_size = 0
    def percolate_up(self,index):
        """Checks the order of the root of a certain index
        of the tree and fixes the order of nodes if they 
        break the heap property. Works up from the node at 
        index"""
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index//2]:
                temp = self.heap_list[index//2]
                self.heap_list[index//2] = self.heap_list[index]
                self.heap_list[index] = temp
            index = index //2
    def insert(self,value):
        """Inserts a value into the heap ensuring the heap
        property is maintained."""
        self.heap_list.append(value)
        self.current_size += 1
        self.percolate_up(self.current_size)
    def percolate_down(self,index):
        """Checks the order of the root of a certain index
        of the tree and fixes the order of nodes if they 
        break the heap property. Works down from the node at 
        index"""
        while (index * 2 ) <= self.current_size:
            mc = self.min_child(index)

            if self.heap_list[index] > self.heap_list[mc]:
                temp = self.heap_list[mc]
                self.heap_list[mc] = self.heap_list[index]
                self.heap_list[index] = temp
            index = mc

    def min_child(self,index):
        """Returns the child of the node at index with the
        minimum value"""
        if (index * 2 + 1) <= self.current_size:
            if self.heap_list[index *2] < self.heap_list[1 + index * 2]:
                return index*2
            else:
                return 1 + index * 2
        else:
            return index*2
    def delete_min(self):
        """Deletes and returns the minimum value in
        the heap and fixes the heap to ensure it is 
        properly ordered"""
        deleted = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.percolate_down(1)
        return deleted
    def build_heap(self,alist):
        """Given alist, the function converts the list
        into a binary heap data structure."""
        index = len(alist)//2
        self.current_size += len(alist)
        self.heap_list = self.heap_list + alist[:]
        while index > 0:
            self.percolate_down(index)
            index -= 1