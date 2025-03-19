class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        start=0
        end = max(nums)
        cap=0

        def is_valid(mid,nums,k):
            count=0
            i=0
            while i < len(nums):
                if nums[i] <= mid:
                    count+=1
                    i+=2
                else:
                    i+=1
                
                if count == k :
                    break
            return count == k


        while  start<=end:
            mid = start + ((end-start)//2)

            if is_valid(mid,nums,k):
                end = mid-1
                cap = mid
            else:
                start = mid+1
        return cap

            


        