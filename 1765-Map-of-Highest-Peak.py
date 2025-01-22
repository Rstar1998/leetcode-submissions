from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
       
        row_l=len(isWater)
        col_l = len(isWater[0])

        output_matrix = [[0 for _ in range(col_l)] for _ in range(row_l)]
        visited_matrix = [[0 for _ in range(col_l)] for _ in range(row_l)]

        que = deque([])

        for i,row in enumerate(isWater):
            for j ,v1 in enumerate(row):
                if v1 == 1 :
                    que.append((i,j))
                    visited_matrix[i][j]=1
                
        

        level=0
        
        while len(que) != 0:
            temp = []
         
            while len(que) != 0:
                temp.append(que.popleft())
           
            for el in temp:
                r= el[0]
                c= el[1]
                
                if r+1 < row_l and visited_matrix[r+1][c] == 0:
                    output_matrix[r+1][c] = level+1
                    que.append((r+1,c))
                    visited_matrix[r+1][c] = 1

                if r-1 >=0 and  visited_matrix[r-1][c] == 0 :
                    output_matrix[r-1][c] = level+1
                    que.append((r-1,c))
                    visited_matrix[r-1][c] = 1

                if c+1 < col_l and visited_matrix[r][c+1] == 0:
                    output_matrix[r][c+1] = level+1
                    que.append((r,c+1))
                    visited_matrix[r][c+1] = 1

                if c-1 >=0 and  visited_matrix[r][c-1] == 0:
                    output_matrix[r][c-1] = level+1
                    que.append((r,c-1))
                    visited_matrix[r][c-1] = 1
           
            level+=1

        return output_matrix

                
              
                 



        