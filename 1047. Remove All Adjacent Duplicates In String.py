class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for ch in s:
            if len(st)>0 and st[-1] == ch:
                st.pop()
                continue
        
            st.append(ch) 
        return ''.join(st)
        