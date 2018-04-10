class  binary_tree:
    """Implementation of a binary tree"""
    def __init__(self,root_obj):
        """Initializes the object with a name for the root node
        as well as two empty child nodes to the left and right"""
        self.key = root_obj
        self.left_child = None
        self.right_child = None
    def insert_left(self,new_node):
        """Adds a new_node as a child node to the left of the 
        root. If there is already a node to the left, that node
        is pushed further down the tree by adding it as the left 
        node of the new node"""
        if self.left_child == None:
            self.left_child = binary_tree(new_node)
        else:
            temp = binary_tree(new_node)
            temp.left_child = self.left_child
            self.left_child = temp
    def insert_right(self,new_node):
        """Adds a new_node as a child node to the right of the 
        root. If there is already a node to the right, that node
        is pushed further down the tree by adding it as the right 
        node of the new node"""
        if self.right_child == None:
            self.right_child = binary_tree(new_node)
        else:
            temp = binary_tree(new_node)
            temp.right_child = self.right_child
            self.right_child = temp
    
    def get_right_child(self):
        """Returns the value of the right child node"""
        return self.right_child

    def get_left_child(self):
        """Returns the value of the left child node"""
        return self.left_child

    def set_root_val(self,obj):
        """Changes the value of the root node to obj"""
        self.key = obj
    
    def get_root_val(self):
        """Returns the value of the root node"""
        return self.key
    def preorder(self):
        """prints out values present in the tree traversing
        in preordered fashion"""
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
                self.right_child.preorder()


