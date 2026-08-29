# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        solution = []
        while queue:
            level = [item for item in queue]
            queue = []
            for item in level:
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            solution.append(level[-1].val)
        return solution