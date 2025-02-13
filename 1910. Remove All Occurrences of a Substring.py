class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        st =[]
        for i in range(len(s)):
            st.append(s[i])

            if len(st) >= len(part) and st[-1] == part[-1]:
                
                if ''.join(st[-len(part):]) == part:
                    j=0
                    while j < len(part):
                        st.pop()
                        j+=1
                    
        return ''.join(st)


                
            
        