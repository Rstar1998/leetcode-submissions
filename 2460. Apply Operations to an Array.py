class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        c=0
        out=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                continue 

            if i == len(nums)-1:
                out[c]=nums[i]
            else:
                if nums[i]==nums[i+1]:
                    out[c]=nums[i]*2
                    nums[i+1]=0
                else:
                    out[c]=nums[i]
                c+=1
        return out
