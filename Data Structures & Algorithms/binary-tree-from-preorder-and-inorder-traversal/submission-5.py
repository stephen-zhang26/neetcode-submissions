# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {v: i for i, v in enumerate(inorder)}   # 值 → 在 inorder 的下标
        self.pre = 0                                   # preorder 的指针

        def build(l, r):                               # 我负责 inorder 的 [l, r] 这段
            if l > r:
                return None

            val = preorder[self.pre]
            self.pre += 1
            root = TreeNode(val)

            m = idx[val]                               # 根在 inorder 的位置

            root.left  = build(l, m - 1)
            root.right = build(m + 1, r)
            return root

        return build(0, len(inorder) - 1)