class Solution:
    def decodeString(self, s: str) -> str:

        st=[]

        for char in s:
            if char != "]":
                st.append(char)
            else:
                ch=""
                while st[-1]!='[':
                    ch=st.pop()+ch
                st.pop()

                num=""

                while st and st[-1].isdigit():
                    num=st.pop()+num
                st.append(ch*int(num))

        return "".join(st)


        