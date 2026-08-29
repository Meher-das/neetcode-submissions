# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        solution = []
        queue = [root]
        while queue:
            level = [item for item in queue]
            queue = []
            for item in level:
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            solution.append([item.val for item in level])
        return solution
