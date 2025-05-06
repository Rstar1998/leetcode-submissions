class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        s=set()

        def dfs(r,c):
            if (r,c) in s:
                return 0

            if r >= row or c >= col or r<0 or c<0 or grid[r][c]==0:
                return 1

            s.add((r,c))

            p = dfs(r+1,c)
            p+= dfs(r-1,c)
            p+= dfs(r,c-1)
            p+= dfs(r,c+1)
            return p



        for i in range(row):
            for j in range(col):
                if grid[i][j]: 
                    return dfs(i,j)
        