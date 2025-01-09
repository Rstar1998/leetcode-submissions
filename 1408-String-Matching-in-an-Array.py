class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output=set()
        n=len(words)
        i=0
        while i <= n-1:
            j=0
            while j <= n-1:
                if j==i or len(words[i]) > len(words[j]):
                    j+=1
                    continue
                
                if words[i] in words[j]:
                    output.add(words[i])
                    break
                    
                j+=1 
            i+=1
        return list(output)
            
        