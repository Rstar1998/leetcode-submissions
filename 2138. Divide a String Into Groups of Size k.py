class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        diff = 0
        if len(s)%k != 0:
            diff = k - ( len(s)%k )
        
        s+= fill * diff

        output = [ ]

        i =0 
        while i < len(s):
            output.append(s[i:i+k])
            i+=k

        return output

      