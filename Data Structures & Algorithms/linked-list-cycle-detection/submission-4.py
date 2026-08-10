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
        j = head

        while True:
            if i.next and i.next.next:
                i = i.next.next 
                j = j.next
                if i == j:
                    return True
            else:
                return False
            