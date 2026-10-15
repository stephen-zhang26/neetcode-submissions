# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return []

        q = deque([root])

        while q:
            level = []

            for i in range(len(q)):        # 这一层有几个
                node = q.popleft()          # 队头出队
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level[-1])      # ← 今天唯一改动：只要最后一个

        return res
        