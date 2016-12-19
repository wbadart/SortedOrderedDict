# test.py
# Test script for SortedorderedDict

from SortedOrderedDict import SortedOrderedDict
import sys
import random
from collections import OrderedDict

# Function called upon error. Prints error message and exits with error code
def test_failure(msg, error_code):
	print(msg)
	sys.exit(error_code)

# Test map by inserting 1 million elements and searching for all of them
print("Testing map functionality (insertions and searches)...")

# Test using empty map
print("\tTesting using empty map...")
map = SortedOrderedDict()
if map.search("test"):
	test_failure("FAILURE: empty map search test failed", 1)

# Test using full map
print("\tTesting using full map...")
map = SortedOrderedDict()
for i in range(1000000):
	map.insert(i, 2*i)

for i in range(1000000):
	value = map.search(i)
	if value != (2*i):
		test_failure("FAILURE: full map search test failed", 1)

# Test sorted iteration
print("Testing sorted iteration...")

# Test using empty map
print("\tTesting using empty map...")
map = SortedOrderedDict()
if map.to_sorted_list():
	test_failure("FAILURE: empty map sorted iteration failed", 2)

# Test using full map
print("\tTesting using full map...")
map = SortedOrderedDict()
for i in range(1000000):
	map.insert(i, 2*i)

sorted_map = map.to_sorted_list()
if len(sorted_map) != 1000000 or sorted(sorted_map) != sorted_map:
	test_failure("FAILURE: map sorted iteration failed", 2)

# Test ordered iteration
print("Testing ordered iteration...")

# Test using empty map
print("\tTesting using empty map...")
map = SortedOrderedDict()
if map.to_ordered_list():
	test_failure("FAILURE: empty map ordered iteration failed", 3)

# Test using single element
print("\tTesting using map with one element...")
map = SortedOrderedDict()
map.insert("test key", "test value")
ordered_list = map.to_ordered_list()
if len(ordered_list) != 1 or ordered_list[0] != ("test key", "test value"):
	print(ordered_list)
	test_failure("FAILURE: single-element map ordered iteration failed", 3)

# Test using full map
print("\tTesting using full map...")
map = SortedOrderedDict()
# Generate random list of elements and insert them into map
elements = OrderedDict()
for i in range(1000000):
	element = (random.randint(0, 1000000), random.randint(0, 1000000))
	elements[element[0]] = element[1]
	map.insert(element[0], element[1])

ordered_list = map.to_ordered_list()
if ordered_list != list(elements.items()):
	print("{} {}".format(len(ordered_list), len(elements)))
	test_failure("FAILURE: full map ordered iteration failed", 3)

print("Tests Completed. All tests passed")
