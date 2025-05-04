class Solution:
    def validPalindrome(self, s: str) -> bool:

        low=0
        high=len(s)-1

        def check_plaindrome(s):
            return s == s[::-1] 


        while low <= high:
            if s[low] == s[high]:
                low+=1
                high-=1
            else:
                return check_plaindrome(s[0:low]+s[low+1:]) or check_plaindrome(s[0:high]+s[high+1:])
        return True

     