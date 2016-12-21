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

# Test reverse sorted iteration
print("Testing reverse sorted iteration...")

# Test using empty map
print("\tTesting using empty map...")
map = SortedOrderedDict()
if map.to_sorted_list(reverse=True):
	test_failure("FAILURE: empty map reverse sorted iteration failed", 3)

# Test using full map
print("\tTesting using full map...")
map = SortedOrderedDict()
for i in range(1000000):
	map.insert(i, 2*i)

reverse_sorted_map = map.to_sorted_list(reverse=True)
if len(reverse_sorted_map) != 1000000 or sorted(reverse_sorted_map)[::-1] != reverse_sorted_map:
	test_failure("FAILURE: map reverse sorted iteration failed", 3)

# Test ordered iteration
print("Testing ordered iteration...")

# Test using empty map
print("\tTesting using empty map...")
map = SortedOrderedDict()
if map.to_ordered_list():
	test_failure("FAILURE: empty map ordered iteration failed", 4)

# Test using single element
print("\tTesting using map with one element...")
map = SortedOrderedDict()
map.insert("test key", "test value")
ordered_list = map.to_ordered_list()
if len(ordered_list) != 1 or ordered_list[0] != ("test key", "test value"):
	print(ordered_list)
	test_failure("FAILURE: single-element map ordered iteration failed", 4)

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
	test_failure("FAILURE: full map ordered iteration failed", 4)

# Test using reverse ordered iteration
print("Testing reverse ordered iteration...")

# Test using empty map
print("\tTesting using empty map...")
map = SortedOrderedDict()
if map.to_ordered_list(reverse=True):
	test_failure("FAILURE: empty map reverse ordered iteration failed", 5)

# Test using single element
print("\tTesting using map with one element...")
map = SortedOrderedDict()
map.insert("test key", "test value")
ordered_list = map.to_ordered_list(reverse=True)
if len(ordered_list) != 1 or ordered_list[0] != ("test key", "test value"):
	test_failure("FAILURE: single-element map reverse ordered iteration failed", 5)

# Test using full map
print("\tTesting using full map...")
map = SortedOrderedDict()
elements = OrderedDict()
for i in range(1000000):
	element = (random.randint(0, 1000000), random.randint(0, 100000))
	elements[element[0]] = element[1]
	map.insert(element[0], element[1])

reversed_elements = list(elements.items())[::-1]
if map.to_ordered_list(reverse=True) != reversed_elements:
	test_failure("FAILURE: full map reverse ordered iteration failed", 5)

# Test removal
print("Testing map functionality (removal)...")

# Test using empty map
print("\tTesting using empty map...")
map = SortedOrderedDict()
try:
	map.remove("sample key")
except:
	test_failure("FAILURE: removal of non-existant key threw exception", 6)

# Test using single element map
print("\tTesting using single element...")
map = SortedOrderedDict()
map.insert("test key", "test value")
map.remove("test key")
if map.search("test key") or map.to_sorted_list() or map.to_ordered_list():
	test_failure("FAILURE: removal from single element map failed", 6)

# Test using full map
print("\tTesting using full map...")
map = SortedOrderedDict()
odds = []
evens = []
for i in range(0, 1000000, 2):
	map.insert(i, i)
	map.insert(i + 1, i + 1)
	odds.append((i + 1, i + 1))
	evens.append((i, i))

for key, value in evens:
	map.remove(key)
	if map.search(key):
		test_failure("FAILURE: removal of key from full map failed", 6)

for key, value in odds:
	if not map.search(key):
		test_failure("FAILURE: search for existing key after removing another key from full map failed", 6)

if map.to_sorted_list() != odds:
	test_failure("FAILURE: sorted iteration after removal from full map failed", 6)

if map.to_ordered_list() != odds:
	test_failure("FAILURE: ordered iteration after removal from full map failed", 6)

print("Tests Completed. All tests passed")
