class Solution:
    def makeFancyString(self, s: str) -> str:
        st=[]

        for el in s:
            if len(st)>=2 and st[-1] == st[-2] == el:
                continue
            st.append(el)
        return ''.join(st)
        