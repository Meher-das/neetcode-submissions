# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        i = head
        if not i.next.next:
            return False
        else:
            j = head.next.next

        while True:
            if i.val == j.val:
                return True
            if not i.next or not j.next.next:
                return False
            i = i.next
            j = j.next.next
        
        return False