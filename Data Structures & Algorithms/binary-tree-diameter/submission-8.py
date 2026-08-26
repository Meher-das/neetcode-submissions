# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def maxDepth(node):
            if not node:
                return 0
            return max(maxDepth(node.left),maxDepth(node.right)) + 1

        def traverse(node):
            length = maxDepth(node.left) + maxDepth(node.right) 
            self.diameter = max(length, self.diameter)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(root)
        
        return self.diameter