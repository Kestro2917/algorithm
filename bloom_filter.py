import hashlib

class BloomFilter:
	def __init__(self, size, num_hashes):
		self.size = size
		self.num_hashes = num_hashes
		self.bit_array = [False] * size

	def add(self, item):
		for i in range(self.num_hashes):
			hash_val = int(hashlib.md5((str(item)+str(i)).encode()).hexdigest(), 16)
			index = hash_val % self.size
			self.bit_array[index] = True

	def contains(self, item):
		for i in range(self.num_hashes):
			hash_val = int(hashlib.md5((str(item)+str(i)).encode()).hexdigest(), 16)
			index = hash_val % self.size
			if not self.bit_array[index]:
				return False
		return True


bloom_filter = BloomFilter(size=100, num_hashes=3)
urls = ["example.com", "stackoverflow.com", "google.com"]

for url in urls:
	bloom_filter.add(url)

print("Is 'example.com' in the Bloom filter?", bloom_filter.contains("example.com"))
print("Is 'facebook.com' in the Bloom filter?", bloom_filter.contains("facebook.com"))

