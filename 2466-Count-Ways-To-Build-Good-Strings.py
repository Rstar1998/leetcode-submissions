#Attempt 1 : Not Accepted 

class Solution:
    def get_combinations(l,stri,zero,one):

        if len(stri) > l:
            return 0

        if len(stri)==l:
            return 1
        
        lc = Solution.get_combinations(l,stri+("0"*zero),zero,one)
        rc = Solution.get_combinations(l,stri+("1"*one),zero,one)

        return lc+rc

        

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        count=0
        for i in range(low,high+1):
            count = count + Solution.get_combinations(i,"",zero,one)
        return count % (10**9 + 7)


# Attempt 2 : Accepted

class Solution:


    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp={}
        def traverse(l):
            if l > high:
                return 0
            if l in dp:
                return dp[l]
            dp[l] = 1 if l >= low else 0
            dp[l] += (traverse(l+zero) + traverse(l+one))%MOD
            
            return dp[l] % MOD

        return traverse(0) 
        #return count % (10**9 + 7)



        


'''
Check the repetations in length calculation which we have optimized via DP
  l=2
  h=3
  z=1
  o=2

                                       0
                    +z = 1                         +o = 2

            +z=2          +0=3              +z=3             +0=4

       +z=3    +0=4     +z=4   +0=5      +z=4   +0=5      +z=5    +0=6
   +z=4  +0=5


'''