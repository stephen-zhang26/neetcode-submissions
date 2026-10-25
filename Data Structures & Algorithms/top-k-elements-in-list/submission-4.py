class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = 1 + count.get(x, 0)
        pairs = []
        for num, c in count.items():
            pairs.append((c, num))
        pairs.sort(reverse = True)
        res = []
        for i in range(k):
            res.append(pairs[i][1])
        return res