class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        used = set()

        def backtrack():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for n in nums:
                if n in used:
                    continue
                cur.append(n)
                used.add(n)

                backtrack()

                cur.pop()
                used.remove(n)
        backtrack()
        return res
        