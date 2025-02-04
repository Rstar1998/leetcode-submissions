class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        max_sum=nums[0]
        current_sum=nums[0]
        start=1
        end =  len(nums)-1

        while start<= end:
            if nums[start-1]<nums[start]:
                current_sum+=nums[start]
                
            else:
                current_sum=nums[start]
                
            max_sum = max(max_sum,current_sum)
            start+=1
        return max_sum
        