from collections import defaultdict

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_l = len(grid)
        col_l = len(grid[0])

        row_cnt=[0]*row_l
        col_cnt=[0]*col_l

        total_server =0 

        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if el==1:
                    row_cnt[i]+=1
                    col_cnt[j]+=1
                    total_server+=1

        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if el==1 and row_cnt[i]==1 and col_cnt[j] ==1:
                    total_server-=1

        return total_server

    
                    




        