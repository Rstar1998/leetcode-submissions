class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum([  1 for i in str(format(n, 'b')) if i == '1'])
