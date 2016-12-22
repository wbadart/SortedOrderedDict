# SortedOrderedDict.py
# Module for a sorted ordered dictionary

import random

# Object to represent a dictionary that is ordered by insertion as well as a sorting of the keys
class SortedOrderedDict:
	def __init__(self, compare_fn=None):
		self.root = None
		self.head = None
		self.tail = None
		self.compare_fn = compare_fn if compare_fn else SortedOrderedDict.less_than

	# Insert a node into the map
	def insert(self, key, value):
		self.root = self._insert_r(self.root, key, value)

	# Search the treap for a given key
	# If found, returns the value. Otherwise, returns None
	def search(self, key):
		node = self._search(key)
		
		return (node.value if node else None)

	# Remove the node with the given key
	# If the key isn't in the tree, simply do nothing
	def remove(self, key):
		# Call recursive removal function
		self.root = self._remove_r(self.root, key)

	# Save the dictionary to a file in YAML format
	def save(self, filepath):
		with open(filepath, 'w+') as f:
			for key, value in self.iteritems_ordered():
				f.write("{}: {}\n".format(key, value))

	# Generator for iterating through items in sorted order
	def iteritems_sorted(self, reverse=False):
		if not reverse:
			for item in self.iteritems_sorted_normal():
				yield item
		else:
			for item in self.iteritems_sorted_reverse():
				yield item

	# Generator for iterating through elements in sorted order
	# Yields a 2-tuple of the format (key, value)
	def iteritems_sorted_normal(self):
		stack = []
		curr = self.root
		
		# Iterate until loop is broken
		while True:
			if curr is not None:
				# Add current node to stack and traverse left
				stack.append(curr)
				curr = curr.left

			elif stack:
				# Yield current element and traverse right
				curr = stack.pop()
				yield (curr.key, curr.value)
				curr = curr.right
			else:
				# If no node is found and stack is empty, traversal is completed
				break

	# Generator or iterating through elements in reverse sorted order
	# Yields a 2-tuple of the format (key, value)
	def iteritems_sorted_reverse(self):
		stack = []
		curr = self.root

		# Iterate until loop is broken
		while True:
			if curr is not None:
				# Add current node to stack and traverse right
				stack.append(curr)
				curr = curr.right
			elif stack:
				# Yield current element and traverse left
				curr = stack.pop()
				yield (curr.key, curr.value)
				curr = curr.left
			else:
				# If no node is found and stack is empty, traversal is completed
				break

	# Returns a list containing the elements in order sorted by key
	def to_sorted_list(self, reverse=False):
		sorted_list = []

		# Iterate through tree using iteritems_sorted_reverse function and add each item to a list
		for key_value_pair in self.iteritems_sorted(reverse=reverse):
			sorted_list.append(key_value_pair)

		return sorted_list

	# Generator for iterating through the map by order of insertion
	def iteritems_ordered(self, reverse=False):
		if not reverse:
			for item in self.iteritems_ordered_normal():
				yield item
		else:
			for item in self.iteritems_ordered_reverse():
				yield item

	# Generator for iterating through the map by order of insertion (first inserted first)
	def iteritems_ordered_normal(self):
		curr = self.head

		# While there is a current node, yield a 2-tuple with the format (key, value)
		while curr:
			yield (curr.key, curr.value)
			curr = curr.next

	# Generator for iterating through the map in reverse by order of insertion (most recently inserted first)
	def iteritems_ordered_reverse(self):
		curr = self.tail

		# While there is a current node, yield a 2-tuple with the format (key, value)
		while curr:
			yield (curr.key, curr.value)
			curr = curr.prev

	# Return a list of the items in the dictionary ordered by order of insertion
	def to_ordered_list(self, reverse=False):
		ordered_list = []
		# Iterate through linked list
		for key_value_pair in self.iteritems_ordered(reverse=reverse):
			# Append the current key value pair to the list
			ordered_list.append(key_value_pair)

		return ordered_list
			

	# Helper function to recursively insert an element into the treap
	def _insert_r(self, node, key, value):
		if not node:
			# If node isnt found in tree, make a new one
			node = Node(key, value)
			
			# Insert into the linked list
			if not self.tail:
				self.head = node
				self.tail = node
			else:
				self.tail.next = node
				node.prev = self.tail
				self.tail = node

			return node

		if key == node.key:
			# If key is already in tree, simply update its value
			node.value = value

		elif self.compare_fn(key, node.key):
			# Traverse left
			node.left = self._insert_r(node.left, key, value)

			# After node is created, check if rotation is necessary
			if node.priority < node.left.priority:
				node = self._rotate_right(node)

		else:
			# Traverse right
			node.right = self._insert_r(node.right, key, value)

			# After node is created, check if rotation is necessary
			if node.priority < node.right.priority:
				node = self._rotate_left(node)

		return node
	# Helper function to search for a given key in the tree
	# If found, returns the node. Otherwise, returns None
	def _search(self, key):
		curr = self.root
		while curr:
			# Iterate through tree using BST properties of treap
			if key == curr.key:
				return curr
			elif self.compare_fn(key, curr.key):
				curr = curr.left
			else:
				curr = curr.right

		return None

	# Recursive helper function to remove a node
	def _remove_r(self, node, key):
		# Base case - if node is empty
		if node is None:
			return node

		# Recurse if node is not being removed
		if self.compare_fn(key, node.key):
			node.left = self._remove_r(node.left, key)
		elif key != node.key:
			node.right = self._remove_r(node.right, key)

		# At this point we know that node will be removed

		# Check if the node doesn't have a left child
		elif node.left is None:
			self._remove_ordering(node)
			node = node.right
		# Check if the node doesn't have a right child
		elif node.right is None:
			self._remove_ordering(node)
			node = node.left
		# If the node has two children, determine which way to rotate
		elif node.left.priority < node.right.priority:
			node = self._rotate_left(node)
			node.left = self._remove_r(node.left, key)
		else:
			node = self._rotate_right(node)
			node.right = self._remove_r(node.right, key)

		return node

	# Function to remove a node from the linked list
	def _remove_ordering(self, node):
		# Input validation
		if self.head is None or node is None:
			return

		if node == self.head and node == self.tail:
			self.head = None
			self.tail = None
		elif node == self.head:
			self.head = self.head.next
			self.head.prev = None
		elif node == self.tail:
			self.tail = self.tail.prev
			self.tail.next = None
		else:
			node.prev.next = node.next
			node.next.prev = node.prev
			
	
	# Function to rotate right at the current node
	def _rotate_right(self, node):
		c = node.left
		t2 = c.right
		c.right = node
		node.left = t2
		return c

	# Function to rotate left at the current node
	def _rotate_left(self, node):
		c = node.right
		t2 = c.left
		c.left = node
		node.right = t2
		return c
	
	# Allow use of in operator
	def __contains__(self, item):
		return True if self._search(item) else False

	@staticmethod
	def less_than(a, b):
		return a < b

# Class to define a node for the SortedOrderedDict
# Uses key, value, priority, left, and right members for treap
# Uses prev and next for ordering by insertion
class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.priority = random.randint(0, 2000000000)
		self.prev = None
		self.next = None
		self.left = None
		self.right = None
