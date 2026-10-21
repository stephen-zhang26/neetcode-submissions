import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]        # 全部取负
        heapq.heapify(heap)

        while len(heap) > 1:          # ① 至少要几块才撞得起来？

            first  = -heapq.heappop(heap)   # ② 最重的（别忘前面的负号）
            second = -heapq.heappop(heap)   # ③ 第二重的

            if first != second:
                heapq.heappush(heap, -(first-second))  # ④ 剩下的差值，存进去要怎么处理？

        return -heap[0] if heap else 0     # ⑤⑥ 剩一块 / 全碎了