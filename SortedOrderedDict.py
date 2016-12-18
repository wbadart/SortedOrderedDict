# SortedOrderedDict.py
# Module for a sorted ordered dictionary

import random

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

	# Helper function to recursively insert an element into the treap
	def _insert_r(self, node, key, value):
		if not node:
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
			node.value = value

		elif self.compare_fn(key, node.key):
			node.left = self._insert_r(node.left, key, value)

			if node.priority < node.left.priority:
				node = self._rotate_right(node)

		else:
			node.right = self._insert_r(node.right, key, value)

			if node.priority < node.right.priority:
				node = self._rotate_left(node)

		return node
	# Helper function to search for a given key in the tree
	# If found, returns the node. Otherwise, returns None
	def _search(self, key):
		curr = self.root
		while curr:
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

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.priority = random.randint(0, 2000000000)
		self.prev = None
		self.next = None
		self.left = None
		self.right = None
