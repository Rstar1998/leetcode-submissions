class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l=0
        r=0
        max_cnt=1
        curr_sum=0
        xor_sum=0

        while(r < len(nums)):

            curr_sum+=nums[r]
            xor_sum^=nums[r]

            while curr_sum!=xor_sum:
                curr_sum-=nums[l]
                xor_sum^=nums[l]  
                l+=1

            max_cnt=max(max_cnt, r-l+1)
            r+=1

            
        
        return max_cnt


        
        