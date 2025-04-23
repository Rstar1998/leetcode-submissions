class Solution:
    def calculate(self, s: str) -> int:
        st=[]
        cur=""
        prev_op="+"
        for i in range(len(s)):
            if s[i].isdigit():
                cur+=s[i]
                
            if ((not s[i].isdigit()) and s[i] != " ") or i == len(s)-1 :
                if prev_op == "-":
                    st.append(-int(cur))
                elif prev_op == "+":
                    st.append(int(cur))
                elif prev_op == "*":
                    st.append(st.pop()*int(cur))
                else:
                    val =st.pop()
                    st.append(math.trunc(val/int(cur)))
                cur=""
                prev_op = s[i]
        
        out=0
        for i in st:
            out+=i
        
        return out


        
            
            


    
        