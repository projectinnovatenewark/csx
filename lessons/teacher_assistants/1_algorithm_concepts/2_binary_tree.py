""" Binary Trees and in-order, pre-order, and post-order traversals"""

# A binary tree is a non-linear data structure comprised of Nodes. Each Node
# has either 0, 1, or 2 children. The root Node is the first node in the binary
# tree and each Node has it's own value, a left pointer, and a right pointer.
# A None value for both the left and right pointer indicates that the Node
# does not have a child. If it only has a None value for one pointer, then it
# has one child. If it has no None values for either pointer, then it has two children.

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

  # Traversals- Traversal operations happen for each node starting with the root. For example,
  # in pre-order if there is a node value, it is printed. Then, it continues to the left node.
  # Then, if there is a node value for that node, it is printed. If that node does not have
  # a left node, then it will continue this operation on the right node. The node will be printed.
  # If that right node does not have any children, it will then propagate back up the tree and
  # perform the same logic for each node.

  # Preorder traversal (N-L-R)
  # Node Root => Left => Right.
  def pre_trav(self, root):
    response_list = []
    if root:
      response_list.append(root.data)
      response_list.extend(self.pre_trav(root.left))
      response_list.extend(self.pre_trav(root.right))
    return response_list

  # Inorder traversal (L-N-R)
  # Left => Node Root => Right.
  def in_trav(self, root):
    response_list = []
    if root:
      response_list.extend(self.in_trav(root.left))
      response_list.append(root.data)
      response_list.extend(self.in_trav(root.right))
    return response_list

  # Postorder traversal (L-R-N)
  # Left => Right => Node Root.
  def post_trav(self, root):
    response_list = []
    if root:
      response_list.extend(self.post_trav(root.left))
      response_list.extend(self.post_trav(root.right))
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

# TITLE: LEVEL ORDER TRAVERSAL FOR INSERTION IN BINARY TREE

"""function to insert element in binary tree"""
def insert(temp,key):
    if not temp:
      root = newNode(key)
      return
    q = []
    q.append(temp)
    # Do level order traversal until we find an empty place.
    while (len(q)):
      temp = q[0]
      q.pop(0)

      if not temp.left:
        temp.left = newNode(key)
        break
      else:
        q.append(temp.left)

      if not temp.right:
        temp.right = newNode(key)
        break
      else:
        q.append(temp.right)