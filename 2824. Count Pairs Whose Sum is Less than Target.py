class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        low=0
        high=len(nums)-1
        count=0

        nums.sort()

        while low < high:
            if nums[low]+nums[high] < target:
                count+=high-low
                low+=1
            else:
                high-=1
        return count

