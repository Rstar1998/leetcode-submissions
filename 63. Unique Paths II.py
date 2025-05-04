class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # count=0
        # m,n = len(obstacleGrid), len(obstacleGrid[0])
        # print(m,n)

        # def backtrack(r,c,obstacleGrid):
        #     nonlocal count
            
        #     if r >= m or c>=n:
        #         return 
            
        #     if obstacleGrid[r][c] == 1:
        #         return
            
        #     if r == m-1 and c==n-1:
        #         count+=1
        #         return
            
        #     backtrack(r+1,c,obstacleGrid) # down
        #     backtrack(r,c+1,obstacleGrid) # right
        
        # backtrack(0,0,obstacleGrid)
        # return count

        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0]*c for _ in range(r)]

        for i in range(r):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0]=1
        
        for i in range(c):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i]=1
        
        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
        return dp[-1][-1]


        