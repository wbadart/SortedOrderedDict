# SortedOrderedDict [![Build Status](https://travis-ci.org/ryansmick/SortedOrderedDict.svg?branch=master)](https://travis-ci.org/ryansmick/SortedOrderedDict)
A python map with a treap backend that can be traversed in sorted order or by order of insertion.

## Complexity

Insertion and search are fairly efficient in the average case because the treap uses probabilistic balancing of the tree. The worst case is the same as that of a binary search tree, but will only occur by random chance rather than a specific order of insertion with the BST. A full table of the complexities of various operations can be seen below.

| Operation         | Average       | Worst |
| ----------------- |:-------------:|:-----:|
| Insert            | O(log n)      | O(n)  |
| Search            | O(log n)      | O(n)  |
| Remove            | O(log n)      | O(n)  |
| Ordered Iteration | O(n)          | O(n)  |
| Sorted Iteration  | O(n)          | O(n)  |

## Usage
In order to use the dictionary, simply clone the repository into your project directory and import the class, as can be seen below.

```
# Clone the repo
$ git clone https://github.com/ryansmick/SortedOrderedDict.git

# Or install via pip:

$ pip install git+https://github.com/ryansmick/SortedOrderedDict.git

# In python file, import the dict
>>> from SortedOrderedDict import SortedOrderedDict

# Create object
>>> map = SortedOrderedDict()

# Optionally pass a compare function if you want a different sorted ordering (default is less-than operator)
>>> map = SortedOrderedDict(compare_fn=custom_compare_function)
```

## Insert, Search, and Remove

Inserting, searching, and removing are fairly simple. You can insert using the *insert* function, which takes the key and value as parameters. Additionally, you can search using the *search* function, which takes the key as a parameter and returns the value corresponding to that key. Searching for a given key will return the associated value if it is found in the dictionary, and will return None otherwise. Finally, you can remove using the *remove* function, which takes the key to remove as a parameter. This will remove the key if it exists, and will do nothing otherwise. Examples of these can be seen below.

```
# Create dict object
>>> map = SortedOrderedDict()

# Insert into object
>>> map.insert("sample key", "sample value")

# Search for key
>>> map.search("sample key")
'sample value'

# Remove the key
>>> map.remove("sample key")
```

## Iteration
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

# PersistentDict
A persistent extension of SortedOrderedDict that has the ability to save and load to and from a YAML file. Since PeristentDict is a subclass of SortedOrderedDict, all functions listed above for SortedOrderedDict will work for PersistentDict, and there are several other functions available only for PersistentDict, which are described below.

## Save and Load Operations
The function definitions for save() and load() can be seen below.

```
# Save function definition
def save(self, save_filepath=None, delim=': ')

# Load function definition
def load(self, filepath, delim=': ', key_trans_func=None, value_trans_func=None, add_to_existing=False)
```

Starting with the save function, the definition is fairly straightforward. It includes optional parameters for save_filepath and delim. You can choose to specify these parameters in the constructor so that ```save()``` performs the same action every time, or you can specify parameters in the function call itself. Additionally, if you specify parameters in the constructor, you can override them by specifying them in the function call.

Note: When using an object with the dictionary, it will be saved as a string using the ```str()``` function to convert the object to a string. In order for this to function properly, the object must have an overloaded``` __str__()``` function that should encode the object as a single line string using a different delimiter between member variables than the dictionary delimiter.

The load function works very similarly, but has some additional parameters. You can use the key_trans_func and value_trans_func parameters to transform the strings read from the file to another data type or to an object type. Additionally, you can optionally use add_to_existing to add the contents of a file to an existing PersistentDict. Otherwise, the dictionary will be cleared before loading the data.

## Context Manager
The PersistentDict class can also be used in a context manager using the "with" keyword. This can be done by passing arguments to the constructor. The benefit of using the class in this way will ensure that your dictionary gets saved to a file before your program quits, no matter what happens during program exexcution. An example can be seen below.

```
# Open the PersistentDict in a context manager
>>> with PersistentDict(save_filepath='/sample/path/map.yml') as map:
...   process()

# Map is automatically saved to file no matter what happens in process()
```
