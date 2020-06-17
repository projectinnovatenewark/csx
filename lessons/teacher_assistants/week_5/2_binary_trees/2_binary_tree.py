# FIXME: write the lesson for binary trees

# FIXME: go over preorder, inorder, and postorder traversals

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        """print the nodes in the tree from left to right"""
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def three_d_print_tree(self, root):
        current_level = [root]
        while current_level:
            print(' '.join(str(node.data) for node in current_level))
            next_level = list()
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right is None and n.left:
                    print('this condition happened')
                    next_level.append(Node(0))
                if n.right:
                    next_level.append(n.right)
            current_level = next_level

    # Preorder traversal (N-L-R)
    # Node Root => Left => Right
    def pre_trav(self, root):
        response_list = []
        if root:
            response_list.append(root.data)
            response_list = response_list + self.pre_trav(root.left)
            response_list = response_list + self.pre_trav(root.right)
        return response_list

    # Inorder traversal (L-N-R)
    # Left => Node Root => Right
    def in_trav(self, root):
        response_list = []
        if root:
            response_list = self.in_trav(root.left)
            response_list.append(root.data)
            response_list = response_list + self.in_trav(root.right)
        return response_list

    # Postorder traversal (L-R-N)
    # Left => Right => Node Root
    def post_trav(self, root):
        response_list = []
        if root:
            response_list = self.post_trav(root.left)
            response_list = response_list + self.post_trav(root.right)
            response_list.append(root.data)
        return response_list

# use insert method to add nodes to the tree [12, 6, 20, 14, 3, 13]
btree = Node(12)
btree.insert(6)
btree.insert(20)
btree.insert(14)
btree.insert(3)
btree.insert(13)
btree.insert(9)

print("print the btree")
btree.print_tree()
print("\n")
print("print the tree layer by layer")
btree.three_d_print_tree(btree)
print("\n")
print("pre-order traversal \n")
print(btree.pre_trav(btree))
print("\n")
print("in-order traversal \n")
print(btree.in_trav(btree))
print("\n")
print("post-order traversal \n")
print(btree.post_trav(btree))
print("\n")

# Depth First Traversals:
# (a) Inorder (Left, Root, Right) : 4 2 5 1 3
# (b) Preorder (Root, Left, Right) : 1 2 4 5 3
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1
