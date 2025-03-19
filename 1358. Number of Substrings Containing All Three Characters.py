from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        h=defaultdict(int)

        l=0
        r=0
        valid_count=0

        while r < len(s):
            h[ s[r] ] += 1

            while h['a'] and h['b'] and h['c']:
                valid_count+= len(s) - r
                h[ s[l] ] -= 1
                l+=1

            r+=1
        return valid_count


        