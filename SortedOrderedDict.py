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

	# Generator for iterating through elements in sorted order
	# Yields a 2-tuple of the format (key, value)
	def iteritems_sorted(self):
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

	# Returns a list containing the elements in order sorted by key
	def to_sorted_list(self):
		sorted_list = []

		# Iterate through tree using iteritems_sorted function and add each item to a list
		for key, value in self.iteritems_sorted():
			sorted_list.append((key, value))

		return sorted_list

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
