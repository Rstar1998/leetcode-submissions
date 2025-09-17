from collections import Counter,defaultdict
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        freq_next = Counter(nums)
     
        freq_prev = defaultdict(int)
        count=0
        for i,elem  in enumerate(nums):
            t = elem * 2

            freq_next[elem]-=1

            if t in freq_next and t in freq_prev:
                count += freq_next[t] * freq_prev[t]
            
            freq_prev[elem]+=1
        return count % (10**9 + 7)




        