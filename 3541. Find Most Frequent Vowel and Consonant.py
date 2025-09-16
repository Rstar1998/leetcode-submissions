from collections import defaultdict
class Solution:
    def maxFreqSum(self, s: str) -> int:

        con = defaultdict(int)
        vov = defaultdict(int)

        max_c = None
        max_v = None

        max_cc = 0
        max_vc = 0

        for ch in s:
            if ch in {'a','e','i','o','u'}:
                vov[ch]+=1
                if vov[ch] > max_vc:
                    max_v=ch
                    max_vc = vov[ch]
            else:
                con[ch]+=1
                if con[ch] > max_cc:
                    max_c=ch
                    max_cc = con[ch]
        return max_cc + max_vc
