class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 1 2 3 5 6
        left=0
        right=left

        count=0

        while left <= right:
            if right >= len(nums):
                count+=1
                break
            if nums[right]-nums[left]<=k:
                right+=1
                continue
            else:
                count+=1
                left=right
        
        return count
            




        
        