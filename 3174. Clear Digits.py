class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        for c in s:
            if c.isalpha():
                st.append(c)
            else:
                st.pop()
        
        return ''.join(st)
        
        