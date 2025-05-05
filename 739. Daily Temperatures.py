class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        out=[0]* len(temperatures)

        for ind , tem in enumerate(temperatures):
            while st and tem > temperatures[st[-1]]:
                idx=st.pop()
                out[idx]=ind-idx
            
            st.append(ind)
        return out
                
        