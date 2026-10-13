# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root                 # 从 CEO 开始

        while cur:
            if p.val > cur.val and q.val > cur.val:      # ① p 和 q 都比 cur 大 → 都在右边
                cur = cur.right           #    往右走

            elif p.val < cur.val and q.val < cur.val:    # ② p 和 q 都比 cur 小 → 都在左边
                cur = cur.left           #    往左走

            else:                      # ③ 分开在两侧了（或其中一个就是 cur）
                return cur          #    cur 就是答案
        