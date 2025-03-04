class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0 :
            return False
            
        temp = n
        while temp%3 == 0:
            temp=temp/3
        return True if temp == 1  else False


   
        