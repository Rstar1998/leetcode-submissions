import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]

        for elm in points:
            d = sqrt(elm[0]**2 + elm[1]**2)
            heapq.heappush(h,(-d,elm))
    
            if len(h) > k:
                heapq.heappop(h)
        out=[]
        for i in h:
            out.append(i[1])
        return out

