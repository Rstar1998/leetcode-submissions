from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # bad_pair_count = 0
        # n= len(nums)
        # for i in range(0,n-1):
        #     for j in range(i+1,n):
        #         if j - i != nums[j] - nums[i]:
        #             bad_pair_count+=1
        # return bad_pair_count
        good_pair=0
        h = defaultdict(int)
        n = len(nums)
        for i in range(n):
            diff = i-nums[i]
            if diff in h:
                good_pair+=h[diff]
            h[diff]+=1
        
        return (n*(n-1)//2)-good_pair




        