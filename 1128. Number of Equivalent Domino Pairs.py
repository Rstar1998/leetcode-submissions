from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        h=defaultdict(int)
        pair=0
        for el in dominoes:
            ab=str(el[0])+"|"+str(el[1]) if el[1] > el[0] else str(el[1])+"|"+str(el[0])
            if ab in h:
                pair+=h[ab]
            h[ab]+=1
        
        return pair


        