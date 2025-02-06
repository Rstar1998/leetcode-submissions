class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        h={}
        count=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]
                if product in h:
                    h[product].append( (i,j) )
                else:
                    h[product]=[(i,j)]
     
        for key,value in h.items():
            if len(value)>=2:
                n=len(value)
                count+= (n*(n-1)//2)*8
        return count

        