    def number_of_leaves(self,root):
        """Additional function for Binary Tree Class,
        given a root Node of a binary tree, returns the
        number of leaves present."""
        leaf = 0
        if self.root:
            if root.left_child:
                leaf += self.number_of_leaves(root.left_child)
            if root.right_child:
                leaf +=self.number_of_leaves(root.right_child)
            if not root.left_child and not root.right_child:
                leaf +=1
        return leaf