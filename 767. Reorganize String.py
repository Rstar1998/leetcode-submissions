import heapq
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:

        h=[]
        dic = Counter(s)
        for k,v in dic.items():
            heapq.heappush(h,(-v,k))
        
        st=""

        while len(h)>1:
            f1,c1=heapq.heappop(h)
            f2,c2=heapq.heappop(h)
            st+=c1+c2
        
            if f1+1 < 0:
                heapq.heappush(h,(f1+1,c1))
            if f2+1 < 0:
                heapq.heappush(h,(f2+1,c2))

        if h:
            f,c = heapq.heappop(h)
            if -f > 1:
                return ""
            st+=c
        return st

