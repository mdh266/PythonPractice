# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        while curr is not None and curr.next is not None:
            temp = curr
            
            while temp.next is not None and temp.next.val == curr.val:
                temp = temp.next
                
            curr.next = temp.next
            curr = curr.next
        
        return head
