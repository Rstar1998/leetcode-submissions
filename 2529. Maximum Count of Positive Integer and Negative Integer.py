class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        def lower_bound(nums,no):
            start=0
            end = len(nums)-1
            while start <= end:
                mid = start + ((end-start)//2)
                if nums[mid] < no:
                    start = mid+1
                else:
                    end = mid -1
            return start
        
        def upper_bound(nums,no):
            start=0
            end = len(nums)-1
            while start <= end:
                mid = start + ((end-start)//2)
                if nums[mid] <= no:
                    start = mid+1
                else:
                    end = mid -1
            return start


        neg = lower_bound(nums,0)
        pos = len(nums) - upper_bound(nums,0) 

        return max(pos,neg)


