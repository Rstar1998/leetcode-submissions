class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        island =0

        def dfs(i,j,grid):
            if i<0 or j <0 or i>= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return  
           
            grid[i][j] = "0"

            dfs(i+1,j,grid)
            dfs(i-1,j,grid)
            dfs(i,j+1,grid)
            dfs(i,j-1,grid)
            

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    island+=1
                    dfs(i,j,grid)
        
        return island

        