from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
	x: Any
	next: Node = None # cant really declare to be Node type


@dataclass
class LinkedList:
	head: Node = None

	def add(self, x: Any) -> None:
		if self.head is None:
			self.head = Node(x)
		else:
			curr = self.head
			while curr.next is not None:
				curr = curr.next

			curr.next = Node(x)

	def remove(self, x) -> None:
		if self.head is None:
			raise Exception("Empty linkedlist!")
		else:
			curr = self.head
			prev = curr
			while curr.next is not None and curr.x != x:
				prev = curr
				curr = curr.next

			if curr.x == x:
				prev.next = curr.next
			else:
				raise Exception(f"{x} is not in the linkedlist!")


	def removeNfromLast(self, N):
		if self.head is None:
			raise Exception("Empty linkedlist!")
		elif self.__len__() < N:
			raise Exception(f"{N} > len(linkedlist)!")
		else:
			curr1 = self.head
			curr2 = self.head

			for i in range(N-1):
				curr2 = curr2.next

			while curr2.next is not None:
				curr1 = curr1.next
				curr2 = curr2.next

			curr1.x = curr1.next.x
			curr1.next = curr1.next.next

	def reverse(self) -> None:
		self._reverse(None, self.head)

	def _reverse(self, prev: Node, curr: Node) -> None:
		if curr is None:
			self.head = prev
		else:
			next_node = curr.next
			curr.next = prev
			self._reverse(curr, next_node)

	def is_palindrome(self):
		if self.__len__() <= 1:
			return True
		else:
			stack = []
			curr = self.head
			while curr.next is not None:
				stack.append(curr.x)
				curr = curr.next
			stack.append(curr.x)

			curr = self.head

			while curr.next is not None:
				if stack.pop() != curr.x:
					return False
				else:
					curr = curr.next

			return True


	def __str__(self) -> str:
		return_val = "" 
		curr = self.head
		while curr.next is not None:
			return_val += f"{curr.x} -> "
			curr = curr.next
		return_val += f"{curr.x}"
		return return_val

	def __len__(self) -> int:
		return_val = 0
		if self.head is not None:
			curr = self.head
			
			while curr.next is not None:
				return_val += 1
				curr = curr.next
		return return_val


if __name__ == "__main__":
	l = LinkedList()
	l.add(5)
	l.add(7)
	l.add("52")

	print(l)

	l.remove(7)
	print(l)

	for i in range(13):
		l.add(i)

	print(l)
	print("len(l) = ", len(l))
	l.removeNfromLast(3)
	print(l)
	l.reverse()
	print(l)

	l1 = LinkedList()
	l1.add(1)
	l1.add(2)
	l1.add(3)
	l1.add(2)
	l1.add(1)

	print(f"{l1} is_palindrome: ", l1.is_palindrome())
	l1.removeNfromLast(1)
	print(f"{l1} is_palindrome: ", l1.is_palindrome())

