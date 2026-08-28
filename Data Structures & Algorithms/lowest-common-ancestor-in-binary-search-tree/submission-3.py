# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def searchSTree(self, node, p, q):
        queue = deque()
        queue.append(node)
        while queue:
            x = queue.popleft()
            if x:
                queue.append(x.left)
                queue.append(x.right)
            
                if x.val == p.val or x.val == q.val:
                    return True
        return False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # print(self.searchSTree(root.left,p,q))
        # print(self.searchSTree(root.right,p,q))
        queue = deque()
        queue.append(root)
        while queue:
            x = queue.popleft()
            if x:
                l = self.searchSTree(x.left,p,q)
                r = self.searchSTree(x.right,p,q)
                # print(x.val,l,r)
                queue.append(x.left)
                queue.append(x.right)
                if x.val == p.val or x.val == q.val:
                    return x
                if l and r:
                    return x
                elif l or r:
                    if x.left and (x.left.val == q.val or x.left.val == p.val): 
                        return x.left
                    if x.right and (x.right.val == p.val or x.right.val == q.val):
                        return x.right
        