# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev = head
        curr = head
        while curr.next is not None:
            prev = curr
            while curr.next is not None and curr.val == prev.val:
                curr = curr.next
            
            if curr.val != prev.val:
                prev.next = curr
            else:
                prev.next = curr
                
        if prev.val == curr.val:
            prev.next = None
            
        return head 
                