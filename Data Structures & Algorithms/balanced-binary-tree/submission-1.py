# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True      # ① 白板初始值
        self.depth(root)
        return self.balanced

    def depth(self, node):
        if not node:
            return 0
        L = self.depth(node.left)
        R = self.depth(node.right)

        if abs(L-R) > 1 :                  # ② 左右深度差超过 1
            self.balanced = False

        return 1 + max(L, R)      # 和刚才一模一样