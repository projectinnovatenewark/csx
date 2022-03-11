"""Linked Lists: Single & Doubly Linked Lists"""

# TITLE: SINGLE LINKED LISTS

# TODO: After each step, put the LinkedList in order as such
# Linked List is 1 -> 2 -> etc..

# class SLLNode:
#   def __init__(self, data = None, next = None):
#     self.data = data
#     self.next = next

#   def list_data(self):
#     print(self.data)
#     if self.next != None:
#       self.next.list_data()

# # Traverse through the SLLNodes with list_data() and print each out
# print("Traverse list of nodes.")
# node1.list_data()

# ####################################################################################################

# # TITLE: DOUBLE LINKED LIST

# class DLLNode:
#   def __init__(self, data = None, next = None, prev = None):
#     self.data = data
#     self.next = next
#     self.prev = prev

#   def list_left_to_right(self):
#     print(self.data)
#     if self.next != None:
#       self.next.list_left_to_right()

#   def list_right_to_left(self):
#     print(self.data)
#     if self.prev != None:
#       self.prev.list_right_to_left()

# # TODO: After each step, put the LinkedList in order as such
# # Linked List is 1 -> 2 -> etc..

# # FIXME: add in steps for creating/updating a node and adjusting the prev and next nodes.

# # Instantiate a Node class
# node1 = DLLNode(2) # Linked List is ___
# print(f"node1.data: {node1.data}")

# # Change node1's data using dot notation and 
# print("Update node1's data attribute (again)")
# node1.data = 9 # Linked List is ___
# print(f"node1.data: {node1.data}")

# # Change node1's next attribute and assign a new DLLNode class to it
# print("Update node1's next attribute")
# node1.next = DLLNode(5) # Linked List is ___
# print(f"node1.next.data: {node1.next.data}")

# # Change node1.next.data using the () method
# print("Update node1.next.data attribute")
# node1.next.(10) # Linked List is ___
# print(node1.next.data)

# # Create new nodes to add further down the nodes' attributes
# node1.next.next = DLLNode(8) # Linked List is ___
# node1.next.next.next = DLLNode(9) # Linked List is ___

# # Traverse through the DLLNodes with list_data() and print each out
# print("Traverse list of nodes.")
# node1.list_data()

# h                   t
# 1 -> 2 -> 3 -> 4 -> 5

class SLLNode:
  def __init__(self, d = None, n = None):
    self.data = d
    self.next = n

  def traverse(self):
    curr_node = self
    while curr_node:
      print(curr_node.data)
      curr_node = curr_node.next
    print("DONE!!!")


  def append(self, nextNode):
    curr_node = self
    while curr_node.next:
      print("curr node: ", curr_node.data)
      curr_node = curr_node.next
    curr_node.next = nextNode

# Instantiate a SLLNode class
node1 = SLLNode(2)
print(f"node1.data: {node1.data}")

# Change node1's data using dot notation
print("Update node1's data attribute (again)")
node1.data = 100
print(f"node1.data: {node1.data}")

# As you can see in the above two examples, you can change an attribute
# in a method by using the "self" object and call that method on the object
# you would like to change (line 24), or you can directly change
# the object's attribute using dot notation (line 29).

# Change node1's next attribute and assign a new SLLNode class to it
print("Update node1's next attribute")
node1.next = SLLNode(5)
print(f"node1.next.data: {node1.next.data}")

# Create new nodes to add further down the nodes' attributes
node1.next.next = SLLNode(8)
node1.next.next.next = SLLNode(9)


node1.append(SLLNode(2))
node1.append(SLLNode(3))
node1.append(SLLNode(4))
node1.append(SLLNode(5))

node1.traverse()
