class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output=[]
        def backtrack(st,o,c,n):

            if len(st) == (2*n):
                output.append(st)
            
            if o < n:
                backtrack(st+"(",o+1,c,n)
            
            if o > c:
                backtrack(st+")",o,c+1,n)

        backtrack("",0,0,n)
        return output
        



        