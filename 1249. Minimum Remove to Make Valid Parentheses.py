class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st=[]
        out_str=list(s)

        for ind,ch in enumerate(s):
            if ch == "(":
                st.append(ind)
            elif ch==")":
                if st:
                    st.pop()
                else:
                    out_str[ind]=''
        while st:
            out_str[st.pop()]=''
        
        return ''.join(out_str)

 