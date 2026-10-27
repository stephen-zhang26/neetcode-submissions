class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(open_n, close_n):
            if open_n == close_n ==n:
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, close_n)
                stack.pop()

            if close_n < open_n:                # 还能放右括号
                stack.append(")")
                backtrack(open_n, close_n + 1)       # ④
                stack.pop()                  # ⑤ 撤销

        backtrack(0, 0)
        return res

        