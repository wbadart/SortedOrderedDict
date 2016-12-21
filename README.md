# SortedOrderedDict [![Build Status](https://travis-ci.org/ryansmick/SortedOrderedDict.svg?branch=master)](https://travis-ci.org/ryansmick/SortedOrderedDict)
A python map with a treap backend that can be traversed in sorted order or by order of insertion.

##Complexity

Insertion and search are fairly efficient in the average case because the treap uses probabilistic balancing of the tree. The worst case is the same as that of a binary search tree, but will only occur by random chance rather than a specific order of insertion with the BST. A full table of the complexities of various operations can be seen below.

| Operation         | Average       | Worst |
| ----------------- |:-------------:|:-----:|
| Insertion         | O(log n)      | O(n)  |
| Search            | O(log n)      | O(n)  |
| Ordered Iteration | O(n)          | O(n)  |
| Sorted Iteration  | O(n)          | O(n)  |

##Usage
In order to use the dictionary, simply clone the repository into your project directory and import the class, as can be seen below.

```
# Clone the repo
$ git clone https://github.com/ryansmick/SortedOrderedDict.git

# In python file, import the dict
>>> from SortedOrderedDict import SortedOrderedDict

# Create object
>>> map = SortedOrderedDict()

# Optionally pass a compare function if you want a different sorted ordering (default is less-than operator)
>>> map = SortedOrderedDict(compare_fn=custom_compare_function)
```

##Insertion and Searching

Insertion and searching are fairly simple. You can insert using the *insert* function, which takes the key and value as parameters. You can search using the *search* function, which takes the key as a parameter and returns the value corresponding to that key. Examples of these can be seen below.

```
# Create dict object
>>> map = SortedOrderedDict()

# Insert into object
>>> map.insert("sample key", "sample value")

# Search for key
>>> map.search("sample key")
'sample value'
```

##Iteration
This is the bread and butter of this data structure because it was designed with versitile iteration in mind. The dictionary can be iterated in sorted order or by order of insertion. A python list can also easily be created from the dictionary in both sorted order and by order of iteration. Examples of this functionality can be seen below.

```
# Create SortedOrderedDict instance and insert several key-value pairs
>>> map = SortedOrderedDict()
>>> map.insert(...)

# Iterate dictionary in sorted order
>>> for key, value in map.iteritems_sorted():
...   process()
  
# Iterate dictionary in reverse sorted order
>>> for key, value in map.iteritems_sorted(reverse=True):
...   process()

# Iterate dictionary by order of iteration (oldest first)
>>> for key value in map.iteritems_ordered():
...   process()

# Iterate dictionary by reverse order of iteration (most recently inserted first)
>>> for key, value in map.iteritems_ordered(reverse=True):
...   process()

# Convert dictionary to list of 2-tuples in (key, value) format in sorted order
# Also supports reverse=True keyword argument
>>> sorted_list = map.to_sorted_list()

# Convert dictionary to list of 2-tuples in (key, value) format ordered by insertion
# Also supports reverse=True keyword argument
>>> ordered_list = map.to_ordered_list()
```
