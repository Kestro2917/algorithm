class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

def inorder_traversal(root):
	if root:
		inorder_traversal(root.left)
		print(root.value, end=" ")
		inorder_traversal(root.right)

def preorder_traversal(root):
	if root:
		print(root.value, end=" ")
		preorder_traversal(root.left)
		preorder_traversal(root.right)

def postorder_traversal(root):
	if root:
		postorder_traversal(root.left)
		postorder_traversal(root.right)
		print(root.value, end=" ")

# Example usage
# Constructing a binary tree

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Traversal the binary tree

print("Inorder Traversal:", end=" ")
inorder_traversal(root)
print("\nPreoder Traversal:", end=" ")
preorder_traversal(root)
print("\nPostorder Traversal:", end=" ")
postorder_traversal(root)
