class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            c = 0
            x = i
            while x:
                c += x &1
                x >>= 1
            ans.append(c)
        return ans

        