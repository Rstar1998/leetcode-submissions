class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first_occurence(nums,target):
            low =0
            high = len(nums)-1
            result = -1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    result = mid
                    high = mid-1
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return result 
        
        def last_occurence(nums,target):
            low =0
            high = len(nums)-1
            result = -1
            while low <= high:
                mid = low + (high-low)//2
                if nums[mid] == target:
                    result = mid
                    low = mid+1
                elif nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return result 
        
        return [ first_occurence(nums,target), last_occurence(nums,target) ]



        