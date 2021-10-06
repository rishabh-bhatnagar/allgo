'''
Time Complexity
Best : O(n log(n))
Average : O(n log(n))
Worst : O(n ^ 2)
'''

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

def insert(root, node):
	if root is None:
		root = node

	else:
		if root.data > node.data:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)
		else:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)

def in_order_traversal(root):
	if not root:
		return
	else:
		in_order_traversal(root.left)
		print(root.data, end=' ')
		in_order_traversal(root.right)


A = [9, 8, 7, 6, 5, 4, 3, 2, 1]

root = Node(A[0])
for i in range(1, len(A)):
	insert(root, Node(A[i]))

in_order_traversal(root)
	

