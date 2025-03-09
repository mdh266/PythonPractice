#!/usr/bin/env/python

class Node:

	def __init__(self, x=None, prev_node=None, next_node=None):
		self.value = x
		self.next_node = next_node
		self.prev_node = prev_node

	def set_value(self,x):
		self.value = x

	def set_next(self, node):
		self.next_node = node
		node.prev_node = self

	def set_prev(self, node):
		self.prev_node = node
		node.next_node = self

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next_node

	def get_prev(self):
		return self.prev_node


class DoubleLinkedList:

	def __init__(self, val=None):
		self.head = Node(val)

	def add_node(self, x):
		if(self.head.get_value() == None):
			self.head = Node(x)
		else:
			curr = self.head
			while(curr.get_next() != None):
				curr = curr.get_next()

			curr.set_next(Node(x))
	
	def size(self):
		curr = self.head
		if curr.get_value() == None:
			return 0
		else:
			N = 1
			while(curr.get_next() != None):
				N += 1
				curr = curr.get_next()
		
			return N

	def insert(self, x, N):
		if(N > self.size()):
			print "list not long enough"
		else:
			before_node = self.head
			for i in range(0,N-1):
				before_node = before_node.get_next()

			before_node.get_value()
			after_node = before_node.get_next()
			before_node.set_next(Node(x))

			after_node.set_prev(before_node.get_next())
			

	def __str__(self):
		string = ""
		curr = self.head
		while(curr != None):
			string += str(curr.get_value())
			curr = curr.get_next()

		return string
	
	def printInReverse(self):
		curr = self.head
		string = ""
		while (curr.get_next() != None):
			curr = curr.get_next()

		# now at tail, 
		while (curr != None):
			string += str(curr.get_value())
			curr = curr.get_prev()

		print string

if __name__ == "__main__":

	x = DoubleLinkedList()
	
	for i in range(0,5):
		x.add_node(i)
	
	print x
	x.printInReverse()
	
	print x.size()
	x.insert(9,4)
	
	print x
	x.printInReverse()
	