# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []                      # 最终结果，装一堆小列表

        if not root:
            return []             # ① 空树 → 返回什么？

        q = deque([root])             # 队列初始：只有 root 一个人

        while q:                      # 队里还有人就继续
            level = []                # 这一层的人，先开个空列表装

            for i in range(len(q)):   # ② 先点人数！这一层有几个？
                node = q.popleft()     # ③ 队头那个出队
                level.append(node.val)

                if node.left:         # 有左孩子才排
                    q.append(node.left)  # ④ 排到队尾
                if node.right:
                    q.append(node.right)

            res.append(level)         # 这一层点完名，装进结果

        return res
        
        