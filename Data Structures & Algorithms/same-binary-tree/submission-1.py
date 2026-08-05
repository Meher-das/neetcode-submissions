# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list_1 = []
        list_2 = []
        def traverseNode(node,tlist):
            if not node:
                x = None
            else:
                traverseNode(node.left,tlist)
                traverseNode(node.right,tlist)
                x = node.val
            tlist.append(x)
        traverseNode(p,list_1)
        traverseNode(q,list_2)
        # print(list_1)
        # print(list_2)
        return list_1 == list_2