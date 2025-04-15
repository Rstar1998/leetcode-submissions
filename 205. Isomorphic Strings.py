from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hs=defaultdict(str)
        ht=defaultdict(str)

        for i in range(0, len(s)):

            if (s[i] in hs and hs[s[i]] != t[i]) or (t[i] in ht and ht[t[i]] != s[i]):
                return False
            else:
                hs[s[i]] = t[i]
                ht[t[i]] = s[i]
        return True

          
     