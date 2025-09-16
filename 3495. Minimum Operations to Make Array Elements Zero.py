import math
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        
        def required(n):
            if n == 0:
                return 0
            x = int(math.log(n, 4)) 
            total = ((4 ** x) * (3 * x - 1)  + 1)/3
            total += (n - 4 ** x + 1) * (x + 1)
            return int(total)

        count = 0
        for l, r in queries: 
            count += (required(r) - required(l - 1) + 1) // 2
        return count
            