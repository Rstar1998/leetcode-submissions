class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        set1 = set(nums)
        set2 = set()
        def backtrack(st,l):

            if len(set2) > len(set1):
                return 
                
            if l==len(nums):
                set2.add(st)
                return 
            

            backtrack(st+"1",l+1)
            backtrack(st+"0",l+1)
            
     
        
        backtrack("",0)
     
        diff = set2.difference(set1)
      
        return (list(diff))[0]

        

        