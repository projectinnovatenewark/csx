"""
Review iterative tree traversals and then move on to recursive implementations
"""
# TODO: add in the Class definition for this algorithm


# We want to use a stack data structure so we can finish each left subtree's operations before moving on to the right subtree,
# given that preorder occurs in the order NLR. As we add nodes to the end of the "current" list, you can observe that the
# LIFO method is used when performing these operations.

def iterativePreorderTraversal(self, root):
    current = [root]
    listy = []
    
    while current:
        curr_node = current.pop()
        if (curr_node):
            listy.append(curr_node.val)
            
            if (curr_node.right):
                current.append(curr_node.right)
            if (curr_node.left):
                current.append(curr_node.left)

    return listy
    
# Now that you understand how the above works iteratively, let's create a recursive implementation.

def recursivePreorderTraversal(self, root):
    if (root):
        listy = [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
            return listy
        else:
            return []
