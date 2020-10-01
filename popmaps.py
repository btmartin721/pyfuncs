
from collections import OrderedDict

class Popmap:
	"""
	Class to handle popmap files.
	"""
	def __init__(self, filename):
		"""
		Instantiate class.
		Input
			filename: string; path to two-column tab-delimited popmap file. Format: indID\tpopID
		"""
		self.filename = filename

	def read_popmap(self):
		"""
		Read a population map file.
		Input:
			self
		Returns:
			results: dict of {indIDs: popIDs}
		"""
		popmap = dict()
		with open(self.filename, "r") as popfile:
			for line in popfile:
				line = line.strip()
				inds, pops = line.split()
				popmap[inds] = pops
		return popmap

	def get_samples_per_pop(self, d):
		"""
		Finds samples associated with each population in the popmap:
		Input:
			d: popmap dictionary {indids: popids}.
		Returns:
			popdict: dictionary {'Pop1': [inds], 'Pop2': [inds]}
		"""
		popdict = dict()

		# Swap keys and values; keys to list of values; values to unique keys.
		for k,v in d.items():
			if v in popdict:
				popdict[v].append(k)
			else:
				popdict[v] = [k]
		return popdict

	def reorder_popdict(self, orderfile, popdict):
		"""
		Reorder populations in custom order using tab-separated input file.
		Input:
			poporder: path to two-column tab-separated file; order(integer)\tpopID
			popdict: Dictionary {popID: [list_of_inds]}
		Returns:
			reordered popdict 
		"""
		poporder = dict()
		with open(orderfile, "r") as po:
			for line in po:
				line = line.strip()
				order, pop = line.split()
				order = int(order)
				poporder[order] = pop

		poporder_sorted = OrderedDict(sorted(poporder.items()))
		poporder_sorted = dict(poporder_sorted)
		poplist_sorted = list(poporder_sorted.values())

		popdict_sorted = OrderedDict([(el, popdict[el]) for el in poplist_sorted])

		return dict(popdict_sorted)

	def print_popcounts(self, popdict):
		# Sanity checks. Print number of individuals in each population.
		print("\nPopulation counts:")
		for k in popdict.keys():
			print("{}: {}".format(k, len(popdict[k])))

	def print_popmap(self, popmap):
		print(popmap)