import heapq

# sample list 
listy = [5, 7, 9, 1, 3]

# TITLE: Python class version of Heap

# Class implementation of Min Heap
class MaxHeap:
	def __init__(self):
		self.heap = []

	# Functions for getting parent/children
	def get_parent(self, i):
		return int((i-1)/2)

	def get_left_child(self, i):
		return 2*i+1

	def get_right_child(self, i):
		return 2*i+2

	# Functions to check if parent/children exist
	def has_parent(self, i):
		return self.get_parent(i) >= 0

	def has_left_child(self, i):
		return self.get_left_child(i) < len(self.heap)

	def has_right_child(self, i):
		return self.get_right_child(i) < len(self.heap)

	# Operations to perform on the heap
	def swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def insert_key(self, key):
		self.heap.append(key)
		last_item_idx = len(self.heap) - 1
		self.heapify_up(last_item_idx)

	def heapify_up(self, i):
		length = len(self.heap)
		while (self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]):
			self.swap(i, self.get_parent(i))
			i = self.get_parent(i)

	def delete_root(self):
		if (len(self.heap) == 0):
			return -1
		last_index = len(self.heap) - 1
		self.swap(0, last_index)
		root = self.heap.pop()
		self.heapify_down(0)
		return root

	def heapify_down(self, i):
		while (self.has_left_child(i)):
			max_child_ind = self.get_max_child_index(i)
			if (max_child_ind == -1):
				break
			if (self.heap[i] < self.heap[max_child_ind]):
				self.swap(i, max_child_ind)
				i = max_child_ind
	
	def get_max_child_index(self, i):
		if(self.has_left_child(i)):
			left_c = self.get_left_child(i)
			if (self.has_right_child(i)):
				right_c = self.get_right_child(i)
				if (self.heap[left_c] > self.heap[right_c]):
					return left_c
				else:
					return right_c
			else:
				return left_c
		else:
			return -1

	def print_heap(self):
		print(self.heap)

max_heap = MaxHeap()
for l in listy:
	max_heap.insert_key(l)

print("Unheaped List")
print(listy)

print("First Heap")
max_heap.print_heap()

print("Insert 8 Heap")
max_heap.insert_key(8)
max_heap.print_heap()

print("Insert 2 Heap")
max_heap.insert_key(2)
max_heap.print_heap()

print("Delete Heap Root")
max_heap.delete_root()
max_heap.print_heap()

# TITLE: Min Heap using heapq package

# using heapify to convert list into heap 
heapq.heapify(listy) 
  
# printing created heap 
print (f"The created heap is : {listy}")
  
# using heappush() to push elements into heap 
# pushes 4 
heapq.heappush(listy, 4) 
  
# printing modified heap 
print(f"The modified heap after push is : {listy}") 
  
# using heappop() to pop smallest element 
print(f"The popped and smallest element is : {heapq.heappop(listy)}") 

# printing modified heap 
print(f"The modified heap after pop is : {listy}") 

# TITLE: Max heap using a modified implementation of heapq package

li = []
# using heapify to convert list into heap 
heapq.heapify(li) 

for l in listy:
  heapq.heappush(li, -1 * l)
# printing created heap 
print (f"The created heap is : {li}")
  
# using heappush() to push elements into heap 
# pushes 4 
heapq.heappush(li, -1 * 4) 
  
# printing modified heap 
print(f"The modified heap after push is : {li}") 
  
# using heappop() to pop smallest element 
print(f"The popped and 'largest' element is : {heapq.heappop(li)}") 

# printing modified heap 
print(f"The modified heap after pop is : {li}") 