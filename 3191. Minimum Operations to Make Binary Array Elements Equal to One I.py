class Solution:
    def minOperations(self, nums: List[int]) -> int:

        start=0
        operations=0
        n= len(nums)
        i=0
        while i  <  n-2:
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                operations+=1
            i+=1
        
        if nums[i] == 0 or nums[i+1] == 0:
            return -1
        else:
            return operations


        

     
