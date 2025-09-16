class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        result = []
        for num in nums:
            result.append(num)
            while len(result) > 1:
                a, b = result[-1], result[-2]
                g = math.gcd(a, b)
                if g > 1:
                    result.pop()
                    result.pop()
                    lcm = a // g * b
                    result.append(lcm)
                else:
                    break
        return result