class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        count=0

        even = 1
        odd  = 0
        pre = 0
        i=0
        while i < len(arr):
            pre = arr[i]+ pre
            if pre %2 == 0:
                count+=odd
                even+=1
            else:
                count+=even
                odd+=1
            
            i+=1
        return count%( 10 ** 9 + 7)




        