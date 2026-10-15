# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, node, maxSoFar):
        if not node:
            return 0              # ① 空的，贡献几个 good？

        count = 0
        if node.val>= maxSoFar:                     # ② 这个节点是 good 吗？
            count = 1

        maxSoFar = max(node.val, maxSoFar) # ③ 更新本子

        count += self.dfs(node.left,  maxSoFar)   # ④ 带着本子往左
        count += self.dfs(node.right, maxSoFar)

        return count
        