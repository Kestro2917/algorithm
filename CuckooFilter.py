import random

class CuckooFilter:
	def __init__(self, capacity, bucket_size, max_kicks):
		self.capacity = capacity
		self.bucket_size = bucket_size
		self.max_kicks = max_kicks
		self.buckets = [[] for _ in range(capacity)]

	def hash_functions(self, item):
		hash1 = hash(item)
		hash2 = hash(hash1)
		return hash1, hash2

	def index(self, hash_val, size):
		return hash_val % size

	def insert(self, item):
		hash1, hash2 = self.hash_functions(item)
		i1, i2 = self.index(hash1, self.capacity), self.index(hash2, self.capacity)
	
		for i in range(self.bucket_size):
			if len(self.buckets[i1]) < self.bucket_size:
				self.buckets[i1].append(item)
				return True
			if len(self.buckets[i2]) < self.bucket_size:
				self.buckets[i2].append(item)

			j = random.choice([i1, i2])
			item, self.buckets[j][random.randrange(self.bucket_size)] = self.buckets[j][random.randrange(self.bucket_size)], item
			i1, i2 = self.index(hash1, self.capacity), self.index(hash2, self.capacity)

			if i == self.max_kicks - 1:
				return False

	def contains(self, item):
		hash1, hash2 = self.hash_functions(item)
		i1, i2 = self.index(hash1, self.capacity), self.index(hash2, self.capacity)
		return item in self.buckets[i1] or item in self.buckets[i2]


	def remove(self, item):
		hash1, hash2 = self.hash_functions(item)
		i1, i2 = self.index(hash1, self.capacity), self.index(hash2, self.capacity)
			
		if item in self.buckets[i1]:
			self.buckets[i1].remove(item)
			return True
		elif item in self.buckets[i2]:
			self.buckets[i2].remove(item)
			return True
		else:
			return False

if __name__ == "__main__":
	cuckoo_filter = CuckooFilter(capacity=100, bucket_size=4, max_kicks=500)
	
	items = [str(i) for i in range(100)]
	for item in items:
		cuckoo_filter.insert(item)

	print("Check if '42' is in the filter:", cuckoo_filter.contains('42'))

	cuckoo_filter.remove('42')

	print("Check if '42' is in the filter after removal:", cuckoo_filter.contains('42'))
