# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.balance = True

    def maxDepth(self, node):
        if not node:
            return 0
        l = self.maxDepth(node.left)
        r = self.maxDepth(node.right)
        if abs(l-r) > 1:
            self.balance = False
        return max(l,r) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDepth(root)
        return self.balance
