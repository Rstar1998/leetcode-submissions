class Solution:
    def smallestNumber(self, pattern: str) -> str:
        output=""
        n=1
        st=[]
        for i in pattern:
            if i == "I":
                temp=str(n)
                while len(st) !=0 :
                    temp=str(n+1)+temp
                    n+=1
                    st.pop()

                output+=temp
                n+=1
            else:
                st.append(i)

        temp = str(n)
        while len(st) !=0 :
            temp=str(n+1)+temp
            n+=1
            st.pop()
        output+=temp
        return output
            






        