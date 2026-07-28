# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        i = list1
        j = list2
        answerlist = []

        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        while True:
            answerlist.append(i.val)
            if i.next:
                i = i.next
            else:
                break
        
        while True:
            answerlist.append(j.val)
            if j.next:
                j = j.next
            else:
                break
        answerlist.sort()

        current = head
        for item in answerlist:
            current.next = ListNode(item)
            current = current.next
        
        return head.next

        