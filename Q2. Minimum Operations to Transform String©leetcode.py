from collections import deque,Counter
class Solution:
    def minOperations(self, s: str) -> int:
        set_chr = set(s)
        if 'a' in set_chr:
            set_chr.remove('a')
        seq = deque(sorted(set_chr))
        print(seq)
        op = 0
        
        if len(seq) == 0:
            return op
      
        
        while True:
            first = seq.popleft()
            if len(seq) == 0:
                op += ord('z') - ord(first)+1
                break
                
            
            next = seq[0]

            op+=ord(next)-ord(first)

        return op
            

            
            
 