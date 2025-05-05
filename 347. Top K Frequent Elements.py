import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=[]
        dic = Counter(nums)
        
        for key,val in dic.items():
            heapq.heappush(h,(val,key))
            if len(h) > k:
                heapq.heappop(h)
        return [ i[1] for i in h]

        