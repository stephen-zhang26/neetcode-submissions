class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n]= count.get(n,0)+1#.get是让他在数组里找n这个数，然后0就是如果没有就返回0
        sorted_item= sorted(count.items(),key = lambda x:x[1], reverse =True)#lambda x:x[1]是让他按照第二个元素来排序，reverse = True是让他倒过来，从大到小
        return [pair[0] for pair in sorted_item[:k]]#返回对应的数字不是次数