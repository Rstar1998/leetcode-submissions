class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(n,d):
            return ((n+1)/(d+1) - (n/d))

        h = [ (-gain(n,d),n,d) for n,d in classes ]
        heapq.heapify(h)

        for _ in range(extraStudents):
            g,n,d = heapq.heappop(h)
            n,d = n+1,d+1
            heapq.heappush( h,  (-gain(n,d),n,d) )

        total  = sum(n/d for _,n,d in h )

        return total / len(classes)


    


     

    