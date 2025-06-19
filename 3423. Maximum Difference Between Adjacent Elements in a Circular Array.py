class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:

        left=0
        right=1
        max_val = float("-inf")
        while left <= len(nums)-1:
            if left == len(nums)-1:
                max_val = max(max_val, abs(nums[0]-nums[left]))
                break
            else:
                max_val = max(max_val, abs(nums[right]-nums[left]))
            left+=1
            right+=1
        

        return max_val


        