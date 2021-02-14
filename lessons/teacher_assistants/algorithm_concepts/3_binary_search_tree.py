"""Binary Search Tree"""

# A binary search tree is very similar in structure to a binary tree. The primary
# difference is that in the binary search tree, the left child is always less than or
# equal to the parent node whereas the right child is always greater than the parent node.

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if (self.data):
            if (data < self.data):
                if (self.left is None):
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif (data > self.data):
                if (self.right is None):
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search_value(self, lookup_value):
        if (lookup_value < self.data):
            if (self.left is None):
                return str(lookup_value)+' Not Found'
            return self.left.search_value(lookup_value)
        elif (lookup_value > self.data):
            if (self.right is None):
                return str(lookup_value)+' Not Found'
            return self.right.search_value(lookup_value)
        else:
            print(str(self.data) + ' is found')

    def traverse_tree_in_order(self):
        if (self.left):
            self.left.traverse_tree_in_order()

        print(self.data)

        if (self.right):
            self.right.traverse_tree_in_order()

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

print(root.search_value(7))
print(root.search_value(14))

root.traverse_tree_in_order()