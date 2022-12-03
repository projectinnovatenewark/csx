"""
Linked Lists: Single & Doubly Linked Lists
Slides: https://docs.google.com/presentation/d/12ZTtT-OSKM3i5LIc6-oxYhg4E8YXQqtLwsRQVTkvfLs/edit?usp=sharing

"""

# TITLE: SINGLE LINKED LISTS

class SLLNode:
  def __init__(self, d = None, n = None):
    self.data = d
    self.next = n

  def append(self, new_data):
    curr_node = self
    while curr_node.next:
      curr_node = curr_node.next
    curr_node.next = new_data

  def traverse(self):
    curr_node = self
    while curr_node:
      print(f"Node: {curr_node.data}")
      curr_node = curr_node.next

# Instantiate a SLLNode class
node1 = SLLNode(2)
print("Define node1's data attribute on initialization")
print(f"node1.data: {node1.data}\n")

# Change node1's data using the change_data() method
print("Update node1's data attribute via 'change_data' method")
node1.change_data(17)
print(f"node1.data: {node1.data}\n")

# Change node1's data using dot notation
print("Update node1's data attribute via dot notation")
node1.data = 100
print(f"node1.data: {node1.data}\n")

# Change node1's next attribute and assign a new SLLNode class to it
print("Update node1's next attribute")
node1.next = SLLNode(5)
print(f"node1.next.data: {node1.next.data}\n")

# Change node1.next.data using the change_data() method
print("Update node1.next.data attribute")
node1.next.change_data(10)
print(f"node1.next.data: {node1.next.data}\n")

# Create new nodes to add further down the nodes' attributes
node1.next.next = SLLNode(8)

# Append a new node by method to the linked list
node1.append(SLLNode(9))

# Traverse through the SLLNodes with traverse() and print each out
print("Traverse list of nodes.")
node1.traverse()
print("\n")

# TODO: [insert problem here from LC to remove element]
# Hint 1: using a while loop (such as the one in traverse method) can help you
# iterate through the SLL to find which element you want to remove.
# Hint 2: if your SLL is 1 -> 2 -> 3 -> 4 -> 5 (next pointer changes to next next)
# Hint 3: if your SLL uses a dummy head like None -> 1 -> 2 -> 3 -> 4 -> 5 , then
# you can use identical logic to remove the head node as you would any other node.

# CHALLENGE: https://leetcode.com/problems/reverse-linked-list/

node1.append(SLLNode(2))
node1.append(SLLNode(3))
node1.append(SLLNode(4))
node1.append(SLLNode(5))

# TITLE: DOUBLE LINKED LIST

class DLLNode:
  def __init__(self, data = None, next = None, prev = None):
    self.data = data
    self.next = next
    self.prev = prev

  def add_next(self, nextNode):
    self.next = nextNode
    nextNode.add_prev(self)

  def add_prev(self, prevNode):
    self.prev = prevNode

class DLL:
  def __init__(self, head=None, tail=None):
    self.head = head
    self.tail = tail

  def append(self, newNode):
    if not self.head:
      self.head = newNode
    elif not self.tail:
      self.head.add_next(newNode)
      self.tail = newNode
    else:
      curr_tail = self.tail
      curr_tail.add_next(newNode)
      self.tail = newNode

  def traverse(self):
    curr_node = self.head
    while curr_node:
      print(f"Node: {curr_node.data}")
      curr_node = curr_node.next

  def reverse_traverse(self):
    curr_node = self.tail
    while curr_node:
      print(f"Node: {curr_node.data}")
      curr_node = curr_node.prev

head = DLL()
head.append(DLLNode(1))
head.append(DLLNode(2))
head.append(DLLNode(3))
head.append(DLLNode(4))
head.append(DLLNode(5))
head.append(DLLNode(3))

print("Traverse!")
head.traverse()
print("\n")
print("Reverse Traverse!")
head.reverse_traverse()

# TODO: Define these methods on DLL - pop (delete by index),
# remove (delete by value), append (add to the tail), prepend (add to the head).

