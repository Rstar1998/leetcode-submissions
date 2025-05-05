import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        h=[]

        for num in nums:
            heapq.heappush(h,int(num))
            if len(h) > k:
                heapq.heappop(h)
        return str(h[0])
           
        