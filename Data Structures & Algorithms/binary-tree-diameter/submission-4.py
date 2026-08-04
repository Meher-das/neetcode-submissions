# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self, maxDiameter = 0):
        self.maxDiameter = maxDiameter

    def depth(self, node):
        if not node:
            return 0
        self.maxDiameter = max(self.maxDiameter, self.depth(node.right) + self.depth(node.left))
        return max(self.depth(node.right), self.depth(node.left)) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.depth(root)

        return self.maxDiameter
        
        
