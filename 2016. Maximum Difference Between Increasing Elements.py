class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_val=-1
        prev_max=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if prev_max> nums[i]:
                max_val=max(max_val,prev_max - nums[i])
            else:
                prev_max=max(nums[i],prev_max)
        return max_val


        