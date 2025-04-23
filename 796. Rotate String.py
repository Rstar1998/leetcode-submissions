class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ch = goal[0]

        search=[]
        for i,c in enumerate(s):
            if c == ch:
                search.append(i)
        
        
        for i in search:
            
            if s[i:]+s[:i] == goal:
                return True
        
        return False

        