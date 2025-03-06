class Solution:
    def coloredCells(self, n: int) -> int:

        return 1 + sum([ 4*i for i in range(1,n)])
        
               
        
        