class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
    
        for el in s:
            
            if el in ['{','(','[']:
                
                st.append(el)
            else:
                if len(st) != 0:
                    top = st[-1]
                    st.pop()
                else:
                    return False
                
                if (el == '}' and top == '{') or (el == ')' and top == '(') or (el == ']' and top == '['):
                    
                    continue
                else:
                    return False
                    
        if len(st) == 0:
            return True
        else:
            return False