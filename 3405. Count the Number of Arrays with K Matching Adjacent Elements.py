class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        def modinv(a, mod):
            return pow(a, mod - 2, mod)

        def comb(n, r, mod):
            if r < 0 or r > n:
                return 0
            num = den = 1
            for i in range(r):
                num = num * (n - i) % mod
                den = den * (i + 1) % mod
            return num * modinv(den, mod) % mod

       
        c = comb(n - 1, k, MOD)
        pow_term = pow(m - 1, n - k - 1, MOD)
        return c * m % MOD * pow_term % MOD



#         def backtrack(arr,k):

#             if len(arr) == n and k==0:
#                 return 1
            
#             if len(arr) > n or k<0:
#                 return 0 

#             su=0
#             for i in range(1,m+1):
#                 arr.append(i)
#                 if arr[-1] == arr[-2]:
#                     su+= backtrack(arr,k-1)
#                 else:
#                     su+= backtrack(arr,k)
#                 arr.pop()
#             return su % (10**9 + 7)
          
#         count=0
#         for i in range(1,m+1):
#             arr=[i]
#             count+=backtrack(arr,k)
        
#         return count%(10**9 + 7)
        
