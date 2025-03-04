import math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        while n>0:
            if n%3 == 2:
                return False
            n=n//3
        return True


        # max_power = math.floor(n ** (1/3))
        # current=0
        # for i in range(max_power,-1,-1):
        #     adder = 3 ** i 
            
        #     if (current+adder) > n:
        #         continue
        #     elif (current+adder) == n:
        #         return True
        #     else:
        #         current+=adder
        # return False
       

        