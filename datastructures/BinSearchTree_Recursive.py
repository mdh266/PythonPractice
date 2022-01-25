from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
	val: Any
	left: Node = None
	right: Node = None

@dataclass
class BST:
	root: Node = None

	def add(self, x: Any) -> None:
		if self.root is None:
			self.root = Node(x)
		else:
			self._add(self.root, x)

	def _add(self, curr: Node, x: Any) -> None:
		if x >= curr.val:
			if curr.right is None:
				curr.right = Node(x)
			else:
				self._add(curr.right, x)
		else:
			if curr.left is None:
				curr.left = Node(x)
			else:
				self._add(curr.left, x)

	def height(self) -> int:
		return self._height(self.root)

	def _height(self, curr: None) -> int:
		if curr is None:
			return 0
		else:
			return 1 + max(self._height(curr.left), 
						   self._height(curr.right))

	def findMin(self) -> Any:
		if self.root is not None:
			return self._findMin(self.root)
		else:
			raise Exception("Tree is Empty")

	def _findMin(self, curr: None) -> Any:
		if curr.left is None:
			return curr.val
		else:
			return self._findMin(curr.left)

	def preOrder(self) -> None:
		if self.root is not None:
			self._preOrder(self.root)
		else:
			raise Exception("Tree is Empty")

	def inOrder(self) -> None:
		if self.root is not None:
			self._inOrder(self.root)
		else:
			raise Exception("Tree is Empty")

	def postOrder(self) -> None:
		if self.root is not None:
			self._postOrder(self.root)
		else:
			raise Exception("Tree is Empty")

	def _inOrder(self, curr: Node) -> None:
		if curr.left is not None:
			self._inOrder(curr.left)

		print(curr.val)

		if curr.right is not None:
			self._inOrder(curr.right)


	def _preOrder(self, curr: Node) -> None:

		print(curr.val)

		if curr.left is not None:
			self._inOrder(curr.left)

		if curr.right is not None:
			self._inOrder(curr.right)

	def _postOrder(self, curr: Node) -> None:
		
		if curr.left is not None:
			self._inOrder(curr.left)

		if curr.right is not None:
			self._inOrder(curr.right)

		print(curr.val)

	def delete(self, x : Any) -> None:
		if self.root is not None:
			self.root = self._delete(self.root, x)
		else:
			raise Exception("Tree is Empty")


	def _delete(self, curr: Node, x: Any) -> Node:
		if x < curr.val:
			curr.left  = self._delete(curr.left, x)
		elif x > curr.val:
			curr.right = self._delete(curr.right, x)
		else:
			# this is node we want to delete

			# if this node has only one child, then have parent
			# point this nodes child instead of it
			if curr.left is None:
				return curr.right
			elif curr.right is None:
				return curr.left
			else:
				curr.val   = self._findMin(curr.right)
				curr.right = self._deleteMin(self.right)
				return curr

	def _deleteMin(self, curr: Node) -> Node:
		if curr.left is None:
			return curr.right
		else:
			curr.left = self._deleteMin(curr.left)
			return curr


if __name__ == "__main__":

	# TREE LOOKS LIKE (NOT FULL AND NOT COMPLETE)
	#								2
	#						 	 / \ 
	#							1   4
	# 					 /   / \ 
	#						0		3  13
	#							    /
	#								 8
	#								/ 
	#							 7
	#							/
	#						 5 	

	x = [2,4, 1,13,8,7,5,3,0]

	bst = BST()
	
	for entry in x:
		bst.add(entry)

	print("In Order")
	bst.inOrder() 
	print("Pre Order")
	bst.preOrder()
	print("Post Order")
	bst.postOrder()


	print("min = \n", bst.findMin())


	print("Tree height = ", bst.height())

	print("Remove 13 and then remove 4.")
	bst.delete(13)

	print("In Order")
	bst.inOrder() 

	bst.delete(4) 
	

	print("inOrder :\n ", bst.inOrder())
