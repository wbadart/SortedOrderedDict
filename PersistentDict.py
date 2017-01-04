# PersistentDict.py
# Implements a class for a Persistent Dictionary that has the ability to save to and load from a YAML file

from SortedOrderedDict import SortedOrderedDict

# Subclass of SortedOrderedDict that has teh ability to save and load to and from a YAML file
# Additionally, implemented functions to allow use with a context manager (i.e. "with PersistentDict(...) as map")
class PersistentDict(SortedOrderedDict):
	def __init__(self, save_filepath=None, save_delim=': ', compare_fn=None, load_filepath=None, load_delim=': ', load_key_trans_func=None, load_value_trans_func=None):
		super(PersistentDict, self).__init__(compare_fn=compare_fn)
		if load_filepath:
			self.load(load_filepath, delim=load_delim, key_trans_func=load_key_trans_func, value_trans_func=load_key_trans_func)
		self.save_filepath = save_filepath
		self.save_delim = save_delim

	# Save the dictionary to a file in YAML format
	def save(self, save_filepath=None, delim=': '):
		if save_filepath:
			filepath = save_filepath
		elif self.save_filepath:
			filepath = self.save_filepath
		else:
			raise ValueError("No save filepath specified. Save filepath must be specified as either constructor parameter or save function parameter")

		with open(filepath, 'w+') as f:
			for key, value in self.iteritems_ordered():
				f.write("{}{}{}\n".format(key, delim, value))

	# Load a previously saved dictionary into a SortedOrderedDict object
	def load(self, filepath, delim=': ', key_trans_func=None, value_trans_func=None, add_to_existing=False):
		with open(filepath, 'r') as f:
			if not add_to_existing:
				self.clear()
			for line in f:
				key, value = line.split(delim, 1)
				value = value.rstrip()
				if key_trans_func:
					key = key_trans_func(key)
				if value_trans_func:
					value = value_trans_func(value)
				self.insert(key, value)

	def __enter__(self):
		# Determine if the user entered a filepath at which to save the file
		if not self.save_filepath:
			raise ValueError("No save filepath specified")
		return self

	def __exit__(self, exception_type, exception_value, traceback):
		self.save(delim=self.save_delim)
