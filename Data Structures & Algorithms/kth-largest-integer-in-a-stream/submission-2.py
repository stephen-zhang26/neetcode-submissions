import heapq as hq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        hq.heapify(self.heap)

        while len(self.heap) > k:
            hq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        hq.heappush(self.heap, val)     # ③ 新数进堆

        if len(self.heap) > self.k:
            hq.heappop(self.heap)          # ④ 超了就弹最小的

        return self.heap[0] 
