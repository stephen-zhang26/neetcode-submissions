class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        res ^= len(nums)
        return res






        # n = len(nums)
        # s = (n*(n+1))//2
        # return s - sum(nums)
        