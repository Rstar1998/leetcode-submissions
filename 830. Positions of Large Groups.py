class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        prev=0
        count=1
        output=[]

        for i in range(1,len(s)):
            if s[i] == s[prev]:
                count+=1
            else:
                if count>=3:
                    output.append([prev,i-1])
                prev=i
                count=1

            if i == len(s)-1 and count>=3:
                output.append([prev,i])
    
        return output

        
        