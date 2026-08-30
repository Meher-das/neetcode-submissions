# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preordtrav(self, node,ans):
        if node:
            self.preordtrav(node.left,ans)
            ans.append(node.val)
            self.preordtrav(node.right,ans)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        self.preordtrav(root,ans)
        # print(ans)
        for i in range(len(ans)):
            if i != len(ans) - 1:
                if ans[i] >= ans[i+1]:
                    return False
        return True