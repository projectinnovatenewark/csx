# # FIXME: show single linked lists and double linked lists here

# # SINGLE LINKED LISTS (source: https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python)

# # A single node of a singly linked list
# class Node:
#     # constructor
#     def __init__(self, data = None, next = None):
#         self.data = data
#         self.next = next

# # A Linked List class with a single head node
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # insertion method for the linked list
#     def insert(self, data):
#         new_node = Node(data)
#         if(self.head):
#             current = self.head
#             while current.next:
#                 current = current.next
#                 current.next = new_node
#         else:
#             self.head = new_node

#     # print method for the linked list
#     def output_list(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next

# # Singly Linked List with insertion and print methods
# LL = LinkedList()
# LL.insert(2)
# LL.insert(4)
# LL.insert(6)
# LL.output_list()

# print(LL.head.data)

####################################################################################################

# DOUBLE LINKED LIST

# A complete working Python program to demonstrate all
# insertion methods

# A linked list node
class Node:
	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None # prev is

# Class to create a Doubly Linked List
class DoublyLinkedList:
	# Constructor for empty Doubly Linked List
	def __init__(self):
		self.head = None

	# Given a reference to the head of a list and an
	# integer, inserts a new node on the front of list
	def insert(self, data):
		# 1. Allocates node
		# 2. Put the data in it
		new_node = Node(data)

		# 3. Make next of new node as head and
		# previous as None (already None)
		new_node.next = self.head

		# 4. change prev of head node to new_node
		if self.head:
			self.head.prev = new_node

		# 5. move the head to point to the new node
		self.head = new_node

	# Given a node as prev_node, insert a new node after
	# the given node
	def insert_after(self, prev_node, data):
		# 1. Check if the given prev_node is None
		if prev_node is None:
			print("the given previous node cannot be NULL")
			return

		# 2. allocate new node
		# 3. put in the data
		new_node = Node(data)

		# 4. Make net of new node as next of prev node
		new_node.next = prev_node.next

		# 5. Make prev_node as previous of new_node
		prev_node.next = new_node

		# 6. Make prev_node the previous of new_node
		new_node.prev = prev_node

		# 7. Change previous of new_nodes's next node
		if new_node.next is not None:
			new_node.next.prev = new_node

	# Given a reference to the head of DLL and integer
	# appends a new node at the end
	def append(self, data):
		# 1. Allocates node
		# 2. Put in the data
		new_node = Node(data)

		# 4. If the Linked List is empty, then make th
		# new node as head
		if self.head is None:
			new_node.prev = None
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while last.next is not None:
			last = last.next

		# 6. Change the next of last node
		last.next = new_node

		# 7. Make last node as previous of new node
		new_node.prev = last

		return

	# This function prints contents of linked list
	# starting from the given node
	def output_list(self, node):
		print("\nTraversal in forward direction")
		while node:
			print(" % d" %(node.data))
			last = node
			node = node.next

		print("\nTraversal in reverse direction")
		while last:
			print(" % d" %(last.data))
			last = last.prev

# Driver program to test above functions

# Start with empty list
dllist = DoublyLinkedList()

# Insert 6. So the list becomes 6->None
dllist.append(6)

# Insert 7 at the beginning.
# So linked list becomes 7->6->None
dllist.insert(7)

# Insert 1 at the beginning.
# So linked list becomes 1->7->6->None
dllist.insert(1)

# Insert 4 at the end.
# So linked list becomes 1->7->6->4->None
dllist.append(4)

# Insert 8, after 7.
# So linked list becomes 1->7->8->6->4->None
dllist.insert_after(dllist.head.next, 8)

print("Created DLL is: ")
dllist.output_list(dllist.head)
