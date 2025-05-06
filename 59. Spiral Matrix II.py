class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[ [0]*n for _ in range(n)]
        top=0
        left=0
        right=n-1
        bottom=n-1
        c=1

        while top<=bottom and left<=right:

            for i in range(left,right+1):
                matrix[top][i]=c
                c+=1
            top+=1

            for i in range(top,bottom+1):
                matrix[i][right]=c
                c+=1
            right-=1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    matrix[bottom][i]=c
                    c+=1
                bottom-=1

            if left <= right:
                for i in range(bottom,top-1,-1):
                    matrix[i][left]=c
                    c+=1
                left+=1
        return matrix
        