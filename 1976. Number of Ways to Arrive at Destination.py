from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        wgraph=defaultdict(list)
        way=[0]*n
        dist=[float('inf')]*n

        for row in roads:
            s=row[0]
            d=row[1]
            w=row[2]

            wgraph[s].append((d,w))
            wgraph[d].append((s,w))

        way[0]=1
        dist[0] =0

        pri=[(0,0)]
        heapq.heapify(pri)

        while len(pri)!=0:
            d,c_n = heapq.heappop(pri)

            if d > dist[c_n]:
                continue

            for neig in wgraph[c_n]:
                neig_d = neig[0]
                neig_w = neig[1]
                nd = d+neig_w
                if nd < dist[neig_d]:
                    dist[neig_d] = nd
                    heapq.heappush(pri, (nd,neig_d) )
                    way[neig_d] = way[c_n]
                elif nd == dist[neig_d]:
                    way[neig_d] = (way[neig_d]+way[c_n] ) % (10**9 + 7)

        return way[n-1]


  

        