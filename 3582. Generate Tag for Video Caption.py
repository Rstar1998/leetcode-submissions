class Solution:
    def generateTag(self, caption: str) -> str:

        arr = caption.strip().split(" ")

        st=[]

        for index, word in enumerate(arr):
            t=""
            
            for index2 , ch in enumerate(word):
                if index2 == 0 and ch.isalpha():
                    if index == 0:
                        t+=ch.lower()
                    else:
                        t+=ch.upper()
                elif ch.isalpha():
                    t+=ch.lower()

            st.append(t)

        return "#"+''.join(st)[:99]
            

        