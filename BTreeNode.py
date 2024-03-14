class BTreeNode:	
	def __init__(self, leaf=True):
		self.keys = []
		self.children = []
		self.leaf = leaf

	def is_full(self, order):
		return len(self.keys) >= order - 1

	def split_child(self, child, index, order):
		new_child = BTreeNode(leaf=child.leaf)
		self.children.insert(index+1, new_child)
		self.keys.insert(index, child.keys.pop(order // 2))
		new_child.keys = child.keys[order // 2:]
		child.keys = child.keys[:order // 2]
		if not child.leaf:
			new_child.children = child.children[order // 2]
			child.children = child.children[:order // 2]

class BTree:
	def __init__(self, order):
		self.root = BTreeNode()
		self.order = order

	def insert(self, key):
		if self.root.is_full(self.order):
			new_root = BTreeNode(leaf=False)
			new_root.children.append(self.root)
			new_root.split_child(self.root, 0, self.order)
			self.root = new_root
		self._insert_non_full(self.root, key)

	def _insert_non_full(self, node, key):
		index = len(node.keys) - 1
		if node.leaf:
			node.keys.append(None)
			while index >= 0 and key < node.keys[index]:
				node.keys[index+1] = node.keys[index]
				index -= 1
			node.keys[index+1] = key

		else:
			while index >= 0 and key < node.keys[index]:
				index -= 1
			index += 1
			if node.children[index].is_full(self.order):
				node.split_child(node.children[index], index, self.order)
				if key > node.keys[index]:
					index += 1
				self._insert_non_full(node.children[index],key)

	def search(self, key):
		return self._search(self.root, key)

	def _search(self, node, key):
		i = 0
		while i < len(node.keys) and key > node.keys[i]:
			i += 1
		if i < len(node.keys) and key == node.keys[i]:
			return True
		elif node.leaf:
			return False
		else:
			return self._search(node.children[i], key)

if __name__ == "__main__":
	b_tree = BTree(order=3)
	keys = [10, 20, 5, 6, 12, 30, 7, 17]

	for key in keys:
		b_tree.insert(key)

	print("Searching for 6:", b_tree.search(6))
	print("Searching for 21:", b_tree.search(21))
