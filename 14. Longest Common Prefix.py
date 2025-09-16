class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        print(strs)

        n = min(len(strs[0]) , len(strs[-1]))
        o=""
        for e in range(0,n):
            if strs[0][e] == strs[-1][e]:
                o+=strs[0][e]
            else:
                break
        return o




        
        
        