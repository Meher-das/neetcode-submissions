# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def bfs(self, node):
        self.treelist = []
        queue = deque()
        queue.append(node)
        while queue:
            n = queue.popleft()
            if n:
                self.treelist.append(n.val)
                queue.append(n.left)
                queue.append(n.right)
            else:
                self.treelist.append(None)

        print(self.treelist)
        return self.treelist            

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.bfs(p) == self.bfs(q)