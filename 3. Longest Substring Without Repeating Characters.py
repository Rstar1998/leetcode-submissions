class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        r=0
        mx = 0
        dic={}

        while r <=len(s)-1:
            if s[r] in dic:
                
                end = dic[s[r]]
                
                while l <= end:
                    del dic[s[l]]
                    l+=1

                dic[s[r]] = r
                mx = max(mx , r-l+1)
            else:
                dic[s[r]] = r
                mx = max(mx , r-l+1)

            r+=1
        return mx



        