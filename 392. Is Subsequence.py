class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_start=0
        t_start=0
        s_end=len(s)-1
        t_end=len(t)-1

        while t_start <= t_end and s_start<= s_end:
            if s[s_start]==t[t_start]:
                s_start+=1
            t_start+=1

        if s_start == len(s):
            return True
        else:
            return False


        