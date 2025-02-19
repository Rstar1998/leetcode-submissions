from sortedcontainers import SortedList
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        output = SortedList()
        charset = ['a', 'b' ,'c']
        def backtrack(st,level):
            if level == n:
                output.add(st)
                return
            
            for i in charset:
                if len(st) ==0 or i != st[-1]:
                    backtrack(st+i,level+1)
    
        
        backtrack("",0)
     
        if k-1 >= len(output):
            return ""
        else:
            return output[k-1]