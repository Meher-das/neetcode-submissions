# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, node):
        if not node:
            return 0
        
        return max(self.maxDepth(node.right), self.maxDepth(node.left)) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        if not root:
            return 0

        diameter = self.maxDepth(root.left) + self.maxDepth(root.right)
        maxDiameter = max(diameter,maxDiameter)
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)

        return maxDiameter
        
        
