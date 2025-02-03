class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        i=0
        max_count = 1
        i_count=1
        d_count=1

        while i <= len(nums)-2:
            if nums[i] == nums[i+1]:
                i_count=1
                d_count=1
            elif nums[i] < nums[i+1]:
                i_count+=1
                d_count=1
            else :
                i_count=1
                d_count+=1
            
            max_count=max(max_count,i_count,d_count) 

            i+=1
        return max_count
    
        