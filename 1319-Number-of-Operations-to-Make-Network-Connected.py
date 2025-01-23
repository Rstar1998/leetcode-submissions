class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1 :
            return -1
        
        G = [ set() for _ in range(n)]

        for pair in connections:
            G[pair[0]].add(pair[1])
            G[pair[1]].add(pair[0])

        component = 0
        visited = [ 0 ] * n

        print(G)

        def dfs(G,visited,i):
            visited[i] = 1
            for j in G[i]:
                if visited[j] == 0:
                    dfs(G,visited,j)

        for i,v in enumerate(visited):
            if v == 0:
                component+=1
                dfs(G,visited,i)
        print(component)
        redundant = len(connections) - ((n-1) - (component-1))

        return ((component-1) if (redundant >= (component-1)) else -1)


        