# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import heapq
class Solution:
    def inord(self, node, ans):
        if node:
            self.inord(node.left,ans)
            ans.append(node.val)
            self.inord(node.right,ans)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        self.inord(root,ans)
        # print(ans)
        return ans[k-1]
