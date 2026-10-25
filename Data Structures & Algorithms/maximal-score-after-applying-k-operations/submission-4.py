import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = [-x for x in nums]
        heapq.heapify(h)
        score = 0

        for i in range(k):
            top = -heapq.heappop(h)
            score += top
            heapq.heappush(h, -math.ceil((top+2)//3))
        return score
