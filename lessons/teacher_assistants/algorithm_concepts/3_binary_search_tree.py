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

    def search_value(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+' Not Found'
            return self.left.search_value(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+' Not Found'
            return self.right.search_value(lkpval)
        else:
            print(str(self.data) + ' is found')

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.search_value(7))
print(root.search_value(14))