# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        listsubtree = []
        listsecondtree = []
        # matchingRoot = None

        def traverseTree(node,treelist):
            if not node:
                x = None
                treelist.append(x)
            else:
                x = node.val
                treelist.append(x)
                traverseTree(node.left,treelist)
                traverseTree(node.right,treelist)

        traverseTree(subRoot,listsecondtree)

        def findMatchingRoot(node):
            if not node:
                x = None
            else:
                x = node.val
                if x == subRoot.val:
                    traverseTree(node,listsubtree)
                    if listsubtree == listsecondtree:
                        return
                findMatchingRoot(node.left)
                findMatchingRoot(node.right)

        findMatchingRoot(root)

        # print(listsubtree,listsecondtree)
        return listsubtree == listsecondtree