"""Binary Search Tree"""

# TITLE: Binary Search Tree

# A binary search tree is very similar in structure to a binary tree. The primary
# difference is that in the binary search tree, the left child is always less than or
# equal to the parent node whereas the right child is always greater than the parent node.

class Node:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  def insert_node(self, data):
    """insert a given value in the tree"""
    if (self.data):
      if (data < self.data):
        if (self.left is None):
          self.left = Node(data)
        else:
          self.left.insert_node(data)
      elif (data > self.data):
        if (self.right is None):
          self.right = Node(data)
        else:
          self.right.insert_node(data)
    else:
      self.data = data

  def search_value(self, lookup_value):
    """search for a given value in the tree"""
    # Base Case #1
    if (lookup_value == self.data):
      return str(self.data) + ' is found'

    if (lookup_value < self.data):
      # Base Case #2
      if (self.left is None):
        return str(lookup_value)+' Not Found'
      
      # If left still exists, continue recursing via search function
      else:
        return self.left.search_value(lookup_value)

    elif (lookup_value > self.data):
      # Base Case #3
      if (self.right is None):
        return str(lookup_value)+' Not Found'
      
      # If right still exists, continue recursing via search function
      else:
        return self.right.search_value(lookup_value)

  def find_minimum(self, parent):
    """return the minimum node in the current tree and its parent"""
    # The parent node is passed in as an argument so that eventually when the leftmost
    # child is reached, the call can return both the parent to the successor and the successor

    if self.left:
      return self.left.find_minimum(self)
    else:
      return [parent, self]

  def delete_node(self, delete_value):
    """delete the node with the given key and return the root node of the tree"""

    if self.data == delete_value:
      # found the node we need to delete

      if self.right and self.left: 
        # get the successor node and its parent 
        [psucc, succ] = self.right.find_minimum(self)

        # splice out the successor
        # (we need the parent to do this) 

        if psucc.left == succ:
          psucc.left = succ.right
        else:
          psucc.right = succ.right

        # reset the left and right children of the successor

        succ.left = self.left
        succ.right = self.right

        return succ                

      else:
        # "easier" case
        if self.left:
          return self.left     # promote the left subtree
        else:
          return self.right    # promote the right subtree 
    else:
      if self.data > delete_value: # delete_value should be in the left subtree
        if self.left:
          self.left = self.left.delete_node(delete_value)
      
      # else the delete_value is not in the tree 
      else:                        # delete_value should be in the right subtree
        if self.right:
          self.right = self.right.delete_node(delete_value)

    return self
 

  def traverse_tree_in_order(self):
    # Recursively navigate to the leftmost node in a tree
    if (self.left):
      self.left.traverse_tree_in_order()

    # Print the leftmost node and then propagate back up the tree
    print(self.data)

    # Once the left side of a subtree and the root of the tree have been
    # traversed, recursively implement the above on the right side of the subtree
    if (self.right):
      self.right.traverse_tree_in_order()

root = Node(12)
root.insert_node(6)
root.insert_node(14)
root.insert_node(8)
root.insert_node(10)
root.insert_node(3)

print(root.search_value(7))
print(root.search_value(14))

print("Traverse tree following a search of 7 and 14")
root.traverse_tree_in_order()

root.delete_node(10)
print("Traverse tree following a deletion of 10")
root.traverse_tree_in_order()
