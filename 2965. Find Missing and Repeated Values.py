class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s=set()
        n =len(grid)**2
        a=None
        for i in grid:
            for j in i:
                if j in s:
                    a=j
                s.add(j)
        return [a, ( n*(n+1)//2 )- sum(s) ]


        