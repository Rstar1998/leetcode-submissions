class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        mx=float("-inf")
        di={}
        sub=[0]
        for i in nums:
            sub.append(sub[-1]+i)
        print(sub)
        while r <= len(nums)-1:
            if nums[r] in di:
                
                prev=di[nums[r]]
                while l <=prev:
                    del di[nums[l]]
                    l+=1
                
                mx = max(mx, sub[r+1]-sub[l] )
                di[nums[r]]=r

            else:
                di[nums[r]] = r
                mx = max(mx, sub[r+1]-sub[l] )

            r+=1
        return mx
    