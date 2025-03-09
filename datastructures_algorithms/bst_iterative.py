from __future__ import annotations
from typing import Any
from dataclasses import dataclass

@dataclass
class TreeNode:
	val: Any
	left: TreeNode = None
	right: TreeNode = None


class BinaryTree(object):

	def __init__(self):
		"""Default constructor."""
		self.root = None
	
	def addNode(self, x):
		"""Adds a node to the tree."""
		if self.root is None:
			self.root = TreeNode(x)
		else:
			curr = self.root
			while True:
				if curr.val > x:
					if curr.left is None:
						curr.left = TreeNode(x)
					else:
						curr = curr.left
				elif curr.val < x:
					if curr.right is None:
						curr.right = TreeNode(x)
					else:
						curr = curr.right
				else:
					break;

	def min(self):
		"""Find the minimum of htis tree."""
		return self._min(self.root)
	
	def _min(self, curr):
		"""Find the minumum node the subtree wtih this node as the root."""
		while curr.left is not None:
			curr = curr.left

		return curr.val

	def _deleteMin(self, curr):
		"""Deletes the minimum of subtree with root as curr and returns the value of 
		the deleted node."""
		# find the minimum
		prev = curr
		while curr.left is not None:
			prev = curr
			curr = curr.left

		# now set the new lowest to be the neighbor of old one
		rval = curr.val
		prev.left = curr.right
		curr = None
		return rval	
	
	def delete(self, x):
		"""Iterative deletely the node with value x."""	
		curr = self.root
		# find the node with the val x
		while curr is not None:
			if curr.val == x:
				break;
			elif curr.val < x:
				prev = curr 
				curr = curr.right
			else:
				prev = curr
				curr = curr.left

		# now found the node with the val
		# deal with case of one child
		if curr.left is  None:
			if prev.left == curr:
				prev.left = curr.right
			else:
				prev.right = curr.right
		elif curr.right is  None:
			if prev.left == curr:
				prevr.left = curr.left
			else:
				prev.right = curr.left
		else: # now two children
			curr.val = self._deleteMin(curr.right)

	def preOrder(self):
		"""Prints the tree in pre order."""
		stack = []
		curr = self.root
		# go down the left side of the tree and print the value of the nodes
		# and pushing the node to the stack.
		while curr is not None:
			stack.append(curr)
			print(curr.val)
			curr = curr.left
		
		# now pop parent node of the last and go the right child
		# go down the left side of the right child and print out the value 
		# on that node and push it onto the stack until hit the end and repeat cycle.
		while len(stack) != 0:
			curr = stack.pop()
			curr = curr.right	
			while curr is not None:
				print(curr.val)
				stack.append(curr)
				curr = curr.left

	def inOrder(self):
		"""Prints the tree in order."""
		stack = []
		curr = self.root
		# go down the left side of the tree and 
		# push the node to the stack.
		while stack is not None:
			stac.append(curr)
			curr = curr.left
		
		# now pop parent node of the last and print its value. Then 
		# go the right child and go down the left side of the right child
		# and push each node onto the stack until hit the end and repeat cycle.
		while len(stack) != 0:
			curr = stack.pop()
			print(curr.val)
			
			curr = curr.right	
			while curr is not None:
				stack.append(curr)
				curr = curr.left

	def postOrder(self):
		"""Prints the tree in post Order recursively."""
		self._postOrder(self.root)

	def _postOrder(self, curr):
		"""Innter recursive call for postOrder."""
		if curr is not None:
			self._postOrder(curr.left)
			self._postOrder(curr.right)
			print(curr.val)


	def DFS(self):
		"""Depth first search, iteratively."""
		curr = self.root
		stack = [curr]
		visited = []
		
		# loop through the children and see which nodes have been visisted
		while len(stack) > 0:
			curr = stack.pop()
			# if this node hasnt been visited added to visited 
			# and add its children to stack
			if curr not in visited:
				visited.append(curr)
				if curr.left is not None:
					stack.append(curr.left)
				if curr.right is not None:
					stack.append(curr.right)
		
		# print the visisted nodes	
		while len(visited)!= 0:
			print(visited.pop(0).val)


	def BFS(self):
		"""Breadth first search, iteratively."""
		curr = self.root
		queue = [curr]
		visited = []
		# loop through the children and see which nodes have been visisted
		while len(queue) != 0:
			curr = queue.pop(0)
			# if this node hasnt been visited added to visited 
			# and add its children to stack
			if curr not in visited:
				visited.append(curr)
				if curr.left is not None:
					queue.append(curr.left)
				if curr.right is not None:
					queue.append(curr.right)

		# print the visisted nodes	
		while len(visited) != 0:
			print(visited.pop(0).val)

if __name__ == "__main__":
	x = [12,9,15,11,10,5]


	tree = BinaryTree()
	for n in x:
		tree.addNode(n)
	print "inOrder: "
	tree.inOrder()
	print "preOrder: "
	tree.preOrder()
	print "postOrder: "
	tree.postOrder()
	
	print "min val:"
	print tree.min()

	print "BFS:"
	tree.BFS()

	print "DFS:"
	print tree.DFS()

	print "Delete 9"
	tree.delete(9)

	print "inOrder: "
	tree.inOrder()
	
	print "BFS: "
	tree.BFS()