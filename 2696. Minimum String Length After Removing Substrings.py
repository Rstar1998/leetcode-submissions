class Solution:
    def minLength(self, s: str) -> int:
        st=[]

        for ch in s:
            if len(st)>0 and ( (st[-1] == 'A' and ch == 'B') or (st[-1] == 'C' and ch == 'D')):
                st.pop() 
                continue
            st.append(ch)
        
        return len(st)
            
