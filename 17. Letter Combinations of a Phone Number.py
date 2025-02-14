class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h={
            2 : ['a','b','c'],
            3 : ['d','e','f'],
            4 : ['g','h','i'],
            5 : ['j','k','l'],
            6 : ['m','n','o'],
            7 : ['p','q','r', 's'],
            8 : ['t','u','v'],
            9 : ['w','x','y','z'],

        }

        
        output=[]

        if len(digits)==0:
            return output
            
        def recursive(string,index,current):
            if index == len(string):
                output.append(current)
                return
            
            for ch in h[int(string[index])]:
                recursive(string,index+1,current+ch)

        recursive(digits,0,"")
        
        return output


        