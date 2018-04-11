from binary_tree import binary_tree

def preorder(tree):
    """Taking a binary tree as input, the function
    prints out values present in the tree traversing
    in preordered fashion"""
    if tree:
        print (tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    """Taking a binary tree as input, the function
    prints out values present in the tree traversing
    in postordered fashion"""
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def inorder(tree):
    """Taking a binary tree as input, the function
    prints out values present in the tree traversing
    in inordered fashion"""
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())
