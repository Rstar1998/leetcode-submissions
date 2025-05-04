#Fast pointer slow pointer
class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_square(n):
            s=0
            while n !=0:
                d=n%10
                s+=d*d
                n=n//10
            return s
        
        sp=n
        fp=sum_of_square(n)
        print(sp,fp)
            
        while True:
            print(sp,fp)
            if fp == 1:
                return True 
            if fp==sp:
                return False
            sp=sum_of_square(sp)
            fp=sum_of_square(sum_of_square(fp))

            