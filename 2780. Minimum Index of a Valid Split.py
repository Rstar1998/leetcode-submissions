from collections import Counter
from sortedcontainers import SortedDict
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        dic1 = Counter(nums)
        dic2 = Counter([])
        
        for i in range(0,len(nums)-1):
            dic1[nums[i]]-=1
            dic2[nums[i]]+=1
       
            if (dic2[nums[i]] * 2) > i+1 and (dic1[nums[i]] * 2) > (len(nums)-(i+1)):

                return i
        
        return -1

            







        