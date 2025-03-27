import math
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        arr=[]
        for row in grid:
            for el in row:
                arr.append(el)
        
        arr=sorted(arr)
        n= len(arr)

        if n == 1:
            return 0

     
        mid= n//2
        
        cnt=0
        
        for el in arr:
            diff = abs(el-arr[mid])
            if diff%x != 0:
                return -1
            
            cnt += diff

        return cnt//x



        
        