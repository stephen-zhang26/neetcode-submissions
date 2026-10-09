# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.depth(root)
        return self.res

    def depth(self, node):
        if not node:
            return 0
        L = self.depth(node.left)
        R = self.depth(node.right)
        self.res = max(self.res, L + R)    # ← 记白板
        return 1 + max(L, R)  