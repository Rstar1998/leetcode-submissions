class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        # create a boolean list to mark primes, assume all are prime initially
        primes = [True] * (right + 1)

        # 0 and 1 are not prime
        primes[0], primes[1] = False, False

        # Sieve of Eratosthenes to mark non-primes
        for i in range(2, int(right ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, right + 1, i):
                    primes[j] = False

        # collect primes in the range [x, y]
        res = [i for i in range(left, right + 1) if primes[i]]

        
        if len(res) >= 2:
            min_diff = float("inf")
            a=None
            b=None
            i =1
            while i <= len(res)-1:
                if res[i] - res[i-1] < min_diff:
                    min_diff=res[i] - res[i-1]
                    a=res[i-1]
                    b=res[i]
                i+=1 
            return [ a,b]
        else:
            return [-1,-1]
        