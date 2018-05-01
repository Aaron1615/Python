class priority_queue:
    """Implementation of a binary heap, a heap data structure
    in the form of a binary tee in which all levels except
    the deepest are filled (shape property) and each key is less than or
    equal to the keys of it's children (heap property).Takes
    key,value pairs assuming integers for keys"""
    
    def __init__(self):
        """Initializes a heap of size zero."""
        self.heap_array = [(0,0)]
        self.current_size = 0

    def build_heap(self,alist):
        """Given alist, the function converts the list
        into a binary heap data structure."""

        self.current_size = len(alist)
        self.heap_array = [(0,0)]
        for tup in alist:
            self.heap_array.append(tup)
        index = len(alist)//2
        while index > 0:
            self.percolate_down(index)
            index -= 1

    def percolate_down(self,index):
        """Checks the order of the root of a certain index
        of the tree and fixes the order of nodes if they 
        break the heap property. Works down from the node at 
        index"""
        while (index * 2 ) <= self.current_size:
            mc = self.min_child(index)
            if self.heap_array[index][0] > self.heap_array[mc][0]:
                temp = self.heap_array[mc]
                self.heap_array[mc] = self.heap_array[index]
                self.heap_array[index] = temp
            index = mc


    def min_child(self,index):
        """Returns the child of the node at index with the
        minimum value"""
        if (index * 2) > self.current_size:
            return -1
        else:
            if index*2 + 1 > self.current_size:
                return index * 2
            else:
                if self.heap_array[index*2][0] < self.heap_array[index*2+1][0]:
                    return index * 2
                else:
                    return index*2 +1

    def percolate_up(self,index):
        """Checks the order of the root of a certain index
        of the tree and fixes the order of nodes if they 
        break the heap property. Works up from the node at 
        index"""
        while index // 2 > 0:
            if self.heap_array[index][0] < self.heap_array[index//2][0]:
                temp = self.heap_array[index//2]
                self.heap_array[index//2] = self.heap_array[index]
                self.heap_array[index] = temp
            index = index //2

    def add(self,k):
        """adds a value into the priority queue ensuring
         the heap property is maintained."""
        self.heap_array.append(k)
        self.current_size += 1
        self.percolate_up(self.current_size)

    def delete_min(self):
        """Deletes and returns the minimum value in
        the heap and fixes the heap to ensure it is 
        properly ordered"""
        deleted = self.heap_array[1][1]
        self.heap_array[1] = self.heap_array[self.current_size]
        self.current_size -= 1
        self.heap_array.pop()
        self.percolate_down(1)
        return deleted

    def is_empty(self):
        if self.current_size ==0:
            return True
        else:
            return False

    def decrease_key(self,val,amount):
        done =False
        index = 1
        my_key = 0
        while not done and index <= self.current_size:
            if self.heap_array[index][1] == val:
                done = True
                my_key = index
            else:
                index +=1
        if my_key > 0:
            self.heap_array[my_key] = (amount,self.heap_array[my_key][1])
            self.percolate_up(my_key)
    
    def __contains__(self,vertex):
        for pair in self.heap_array:
            if pair[1] == vertex:
                return True
        return False
