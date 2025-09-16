class Solution:
    def freqAlphabets(self, s: str) -> str:

        st = []

        for ch in s:
            if ch == "#" and len(st)>=2:
                digit1 =st[-1]
                st.pop()
                digit2 =st[-1]
                st.pop()
                st.append(digit2 + digit1 )
                continue
            st.append(ch)
        out=""

        for num in st:
            out+= chr(96+int(num))

        return out

    
        