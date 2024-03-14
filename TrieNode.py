class TrieNode:
	def __init__(self):
		self.children = {}
		self.is_end_of_word = False

class Trie:
	def __init__(self):
		self.root = TrieNode()
		
	def insert(self, word):
		node = self.root
		for char in word:
			if char not in node.children:
				node.children[char] = TrieNode()
			node = node.children[char]
		node.is_end_of_word = True

	def search(self, word):
		node = self.root
		for char in word:
			if char not in node.children:
				return False
			node = node.children[char]
		return node.is_end_of_word

	def starts_with(self, prefix):
		node = self.root
		for char in prefix:
			if char not in node.children:
				return False
			node = node.children[char]
		return True

if __name__ == "__main__":
	trie = Trie()
	
	words = ["apple", "banana", "app", "orange", "applet"]
	for word in words:
		trie.insert(word)

	print("Search for 'apple':", trie.search("apple"))
	print("Search for 'orange':", trie.search("orange"))
	print("Search for 'graph':", trie.search("grape"))

	print("Search with 'app':", trie.starts_with("app"))
	print("Search with 'ban':", trie.starts_with("ban"))
	print("Search with 'gr':", trie.starts_with("gr"))
