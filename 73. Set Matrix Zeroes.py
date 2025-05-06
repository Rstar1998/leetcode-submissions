class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=set()
        c=set()

        for ri,row in enumerate(matrix):
            for ci,el in enumerate(row):
                if el==0:
                    r.add(ri)
                    c.add(ci)
        
        for ri in r:
            for t in range(len(matrix[0])):
                matrix[ri][t]=0
        for ci in c:
            for t in range(len(matrix)):
                matrix[t][ci]=0
        return matrix

        