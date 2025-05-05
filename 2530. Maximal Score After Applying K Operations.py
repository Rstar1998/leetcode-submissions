import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h=[]
        score=0
        for el in nums:
            heapq.heappush(h,-el)

        while k > 0:
            val = heapq.heappop(h)
            pos_val=(-1*val)
            score+= pos_val
            heapq.heappush(h, -1* ceil(pos_val/3) )
            k-=1
        return score

        