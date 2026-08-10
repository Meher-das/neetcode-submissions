# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        before = self.head
        current = self.head.next
        after = current.next

        before.next = None
        while after != None:
            current.next = before
            before = current
            current = after
            after = after.next

        return current
