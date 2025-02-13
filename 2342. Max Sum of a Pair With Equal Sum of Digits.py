from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        h=defaultdict(SortedList)

        for i in range(len(nums)):
            sum_digit = 0
            num=nums[i]
            while num !=0:
                sum_digit+=num%10
                num=num//10

            h[sum_digit].add(nums[i])

        max_num=-1
        for k,v in h.items():
            if len(v)>=2:
                max_num=max(max_num,v[-2]+v[-1])
        return max_num

        

            
        