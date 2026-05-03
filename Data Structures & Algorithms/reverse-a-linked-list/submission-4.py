# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        prev = head

        if head.next == None:
            return head
        current = prev.next
        
        nxt = current.next

        prev.next = None
        while nxt != None:
            current.next = prev
            prev = current
            current = nxt
            nxt = nxt.next
        current.next = prev
        return current
