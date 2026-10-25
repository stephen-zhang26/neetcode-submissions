class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        best = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                best = min(best, right - l + 1)
                total -= nums[l]
                l += 1
        return 0 if best == float('inf') else best


        