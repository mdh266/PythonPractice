class Node:
	
	def __init__(self,val=None, node=None):
		self.value = val
		self.next_node = node


class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        curr = self.head
        if curr is not None:
            string = "["
        while curr.next is not None:
            string +=  str(curr.val) + ", "
            curr = curr.next
        return string + str(curr.val) + "]"
    
    def add(self, x):
        self.head = self._add(x,self.head)
   
    def _add(self, x, curr):
        if curr is None:
            return Node(x)
        else:
            curr.next = self._add(x, curr.next)
            return curr
        
    def delete(self, x):
        """Assumes x is in the list."""
        self._delete(x, self.head)
        
    def _delete(self, x, curr):
        """Asssumes x is in the list."""
        if curr.val == x:
            return curr.next
        else:
            curr.next = self._delete(x, curr.next)
            return curr
        