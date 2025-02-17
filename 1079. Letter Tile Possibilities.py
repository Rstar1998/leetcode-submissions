from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(list(tiles))
        
        node = [0]*26

        for k,v in cnt.items():
            node[ord(k)-ord('A')]+=v

        def recursion(node):
            ways =0
            for i in range(0,26):
                if node[i]>0:
                    node[i]-=1
                    ways += 1 + recursion(node)
                    node[i]+=1
            return ways

        return recursion(node)
        

        