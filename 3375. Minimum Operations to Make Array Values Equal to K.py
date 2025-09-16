from collections import Counter

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        f = Counter(nums)
        op=0
        h= []

        for key,v in f.items():
            heapq.heappush(h,(-key,-v))

        while len(h)>=2:
      
            large = heapq.heappop(h)
            small = heapq.heappop(h)

            if -large[0]<=k:
                return -1
            
            heapq.heappush(h,(small[0],-( (-small[1]) + (-large[1]))))
            op+=1
        
        
        last = heapq.heappop(h)
        if -last[0] == k:
            return op
        elif -last[0] < k:
            return -1
        else:
            return op+1

   
        

    
