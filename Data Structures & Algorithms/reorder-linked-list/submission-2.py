# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue = deque()
        node = head
        while node:
            queue.append(node)
            node = node.next

        i = 0
        j = len(queue) - 1

        curr = ListNode()
        n = len(queue)
        i = 0
        while i < n:
            if i % 2 == 0:
                x = queue.popleft()
            else:
                x = queue.pop()
            curr.next = x
            curr = curr.next
            i += 1
        curr.next = None

        


        
            