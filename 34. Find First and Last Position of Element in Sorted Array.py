class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        ind=-1
        while left <=right:
            mid = (left+right)//2
            if nums[mid] == target:
                ind=mid
                break
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        if ind == -1:
            return [-1,-1]
        else:
            mx=ind
            mn=ind
            while mx+1 < len(nums) and nums[mx+1] == target:
                mx+=1
            while mn-1 >= 0 and nums[mn-1] == target:
                mn-=1
            return [mn,mx]
        