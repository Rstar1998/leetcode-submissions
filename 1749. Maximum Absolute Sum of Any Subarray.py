class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        min_value=0
        max_value=0
        pre=0
        max_sum = float('-inf')

        i = 1
        while i <= len(nums):
            current_sum = nums[i-1]+pre
            pre=current_sum

            max_sum = max(max_sum,max(abs(current_sum - min_value) , abs(current_sum - max_value)))
            min_value = min(min_value,current_sum)
            max_value = max(max_value,current_sum)
            i+=1

        return max_sum
        