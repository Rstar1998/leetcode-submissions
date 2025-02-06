class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        
        start = 0
        end = len(s1)-1
        
        h={}
        mis_count=0
        while start <= end:
            if s1[start] != s2[start]:
                mis_count+=1
                h[ s1[start] ] = s2[start]
            start+=1
        
        if mis_count == 0 or ( mis_count == 2 and sorted(h.keys()) == sorted(h.values()) ) :
            return True
        else:
            return False