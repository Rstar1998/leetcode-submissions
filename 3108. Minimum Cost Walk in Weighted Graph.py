from collections import defaultdict
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        v=[0]*n
        c={}

        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]
            graph[v1].add(v2)
            graph[v2].add(v1)

        comp_cnt=1

        def dfs(i,comp_cnt,v,c):
            v[i] = 1
            c[i] = comp_cnt

            
            for j in graph[i]:
                if v[j] == 0:
                    dfs(j,comp_cnt,v,c)

        for i in range(0,n):
            if v[i] == 0:
                dfs(i,comp_cnt,v,c)
                comp_cnt+=1
        
        comp_and={}
        for i in range(1,comp_cnt):
            comp_and[i] = 2**31 -1 
        
        for edge in edges:
            v1 = edge[0]
            v2 = edge[1]
            comp_and[ c[v1] ] = comp_and[ c[v1] ] & edge[2]
        
        outp=[]

        for q in query:
            v1 = q[0]
            v2 = q[1]
            if v1 == v2:
                outp.append(0)
            elif c[v1] == c[v2]:
                outp.append( comp_and[ c[v1] ] )
            else:
                outp.append(-1)

        return outp




            

        