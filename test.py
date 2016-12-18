# test.py
# Test script for SortedorderedDict

from SortedOrderedDict import SortedOrderedDict
import sys

# Function called upon error. Prints error message and exits with error code
def test_failure(msg, error_code):
	print(msg)
	sys.exit(error_code)

# Test map by inserting 1 million elements and searching for all of them
print("Testing map functionality (insertions and searches)...")
map = SortedOrderedDict()
for i in range(1000000):
	map.insert(i, 2*i)

for i in range(1000000):
	value = map.search(i)
	if value != (2*i):
		test_failure("FAILURE: map search functionality failed", 1)
