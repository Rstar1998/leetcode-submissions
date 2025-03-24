from collections import defaultdict ,Counter
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        v = [0] * n
        

        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]
            graph[v1].add(v2)
            graph[v2].add(v1)

        comp=0

        def dfs(i,v,graph,comp):
            v[i]=comp
            for ed in graph[i]:
                if v[ed]==0:
                    dfs(ed,v,graph,comp)


        for i in range(0,n):
            if v[i] == 0:
                comp+=1
                dfs(i,v,graph,comp)
        
        comp_edge={}
        for i in range(1,comp+1):
            comp_edge[i]=0

        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]
            comp_edge[v[v1]]+=1

        comp_out=0
        node_freq = Counter(v)

        print(node_freq)
        print(comp_edge)

        for k,value in comp_edge.items():
            if value == 0 or value  == (node_freq[k]*(node_freq[k]-1)//2):
                comp_out+=1


        
        return comp_out
            




        