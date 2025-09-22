from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        freq = Counter(nums)

        mx = max(freq.values())

        su=0

        for k,v in freq.items():
            if v == mx:
                su+=v
        return su

