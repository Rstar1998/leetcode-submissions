class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output_set=set()
        nums.sort()

        i=0
        while i <= len(nums)-3:
            start=i+1
            end=len(nums)-1
            if i> 0 and nums[i] == nums[i-1]:
                i+=1
                continue 

            while start < end:
                temp_sum = nums[i]+ nums[start]+nums[end]
                if temp_sum == 0:
                    output_set.add( (nums[i],nums[start],nums[end]) )
                
                if temp_sum < 0:
                    start+=1
                else:
                    end-=1
            i+=1
        return [ list(i) for i in output_set ]
                

        