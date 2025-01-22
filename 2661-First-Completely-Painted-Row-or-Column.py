class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        h={}
        for i,row in enumerate(mat):
            for j,el in enumerate(row):
                h[el]=(i,j)

        row_l = len(mat)
        col_l = len(mat[0])
        row={}
        column={}


        for index,i in enumerate(arr):
            r= h[i][0]
            c= h[i][1]
            if r in row:
                row[r]+=1
                
            else:
                row[r]=1

            if c in column:
                column[c]+=1
            else:
                column[c]=1

            if row[r] == col_l or column[c] == row_l:
                return index

            

            

        
        
        