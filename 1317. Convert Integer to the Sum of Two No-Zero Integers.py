class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        for i in range(1,(n//2)+1):
            a = i
            b = n-i

            if "0" not in str(a) and "0" not in str(b):
                return [a,b]
        return [-1.-1]




        