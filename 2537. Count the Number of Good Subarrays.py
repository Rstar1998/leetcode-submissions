from collections import deque, defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        start = 0
        end = 0
        temp_k=0
        dic = defaultdict(deque)
        out=0

        while end < len(nums):
            if nums[end] in dic:
                temp_k+= len(dic[ nums[end] ])
                dic[ nums[end] ].append(end)
            else:
                dic[ nums[end] ]= deque([ end ] )
            
            while temp_k >= k:
                out+= len(nums) - end

                if nums[start] in dic:
                    if len(dic[nums[start]])>1:
                        dic[nums[start]].popleft()
                        temp_k-=len(dic[ nums[start] ])
                    else:
                        del dic[nums[start]]
                        
                start+=1

            end+=1
        return out







       

        