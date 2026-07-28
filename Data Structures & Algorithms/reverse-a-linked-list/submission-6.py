# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        value_list = []
        while True:
            value_list.append(current.val)
            if not current.next:
                break
            current = current.next
        
        new_head = ListNode()
        current = new_head
        while value_list:
            current.next = ListNode(value_list.pop(-1))
            current = current.next

        return new_head.next