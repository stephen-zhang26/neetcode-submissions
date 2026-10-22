class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            require = target - n
            if require in seen:
                return [seen[require],i]
            seen[n] = i