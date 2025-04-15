from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        ha = {}
        
        for i,v in enumerate(s):
            if v in ha:
                ha[v][1] = i
            else:
                ha[v]=[i,i]
        
        intv = list(ha.values())
        
        merg=[]

        curr=intv[0]

        for i in range(1,len(intv)):
            nex = intv[i]

            if nex[0] < curr[1]:
                curr[1] = max(nex[1],curr[1])
            else:
                merg.append(curr)
                curr = nex
        merg.append(curr)

        out=[]

        for i in merg:
            out.append(i[1]-i[0]+1)

        return out


        





        