# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head_val = None
        x = list1
        y = list2

        if x.val < y.val:
            head_val = x.val
            x = x.next
        else:
            head_val = y.val
            y = y.next

        outHead = ListNode(head_val)
        z = outHead

        while x or y:
            if x.val < y.val:
                temp = x.val
                if x.next:
                    x = x.next
            else:
                temp = y.val
                if y.next:
                    y = y.next

            z.next = ListNode(temp)
            z = z.next
        
        return outHead


    
