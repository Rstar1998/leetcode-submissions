class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def calulate_score(fc,sc,value,s):
            st=[]
            score=0
            for  e in s:
                if len(st) >= 1:
                    if st[-1] == fc and e == sc:
                        st.pop()
                        score+=value
                    else:
                        st.append(e)
                    continue
                else:
                    st.append(e)
            return ''.join(st),score
        
        if y >x :
            st , score1 = calulate_score('b','a',y,s)
            st , score2 = calulate_score('a','b',x,st)
            return score1+score2
        else:
            st , score2 = calulate_score('a','b',x,s)

            st , score1 = calulate_score('b','a',y,st)
           
            return score1+score2


       


        