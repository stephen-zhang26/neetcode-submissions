# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return
            res = inorder(root.left)
            if res is not None:
                return res
            self.k -= 1
            if self.k == 0:
                return root.val
            else:
                return inorder(root.right)
        
        self.k = k
        return inorder(root)
            