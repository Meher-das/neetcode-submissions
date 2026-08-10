# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        newhead = ListNode()
        list1 = []
        list2 = []
        while True:
            if head:
                list1.append(head.val)
            else:
                break

            if head.next:
                list2.append(head.next.val)
            else:
                break

            if head.next.next:
                head = head.next.next
            else:
                break
        print(list2, list2)