class Solution:
    def punishmentNumber(self, n: int) -> int:

        def backtrack(num,rem): 
            if rem == 0 and len(num) == 0:
                return 1
            
            if rem < 0 : 
                return 0

            ans = 0
            for j in range(len(num)):
                pre = num[0:j+1]
                post = num[j+1:]
        
                ans = ans | backtrack(post,rem-int(pre))
            return ans
            
        output=0
        for i in range(1,n+1):
            if backtrack(str(i*i),i) == 1:
                print(i)
                output+=(i*i)
        return output

