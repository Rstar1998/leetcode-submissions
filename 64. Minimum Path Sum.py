class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # global_min=float("inf")
        # m,n = len(grid), len(grid[0])
        # print(m,n)

        # def backtrack(r,c,curr_sum,grid):
        #     nonlocal global_min

        #     if curr_sum > global_min:
        #         return
            
        #     if r >= m or c>=n:
        #         return 
            
        #     if r == m-1 and c==n-1:
        #         global_min=min(global_min,curr_sum+grid[r][c])
        #         return
            
        #     backtrack(r+1,c,curr_sum+grid[r][c],grid) # down
        #     backtrack(r,c+1,curr_sum+grid[r][c],grid) # right
        
        # backtrack(0,0,0,grid)
        # return global_min

        m,n = len(grid), len(grid[0])

        for i in range(1,len(grid)):
            grid[i][0] = grid[i][0]+grid[i-1][0]
        
        for i in range(1,len(grid[0])):
            grid[0][i] = grid[0][i]+grid[0][i-1]

        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        
        return grid[m-1][n-1]
                

        

        


        