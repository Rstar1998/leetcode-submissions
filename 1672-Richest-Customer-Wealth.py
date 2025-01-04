class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_=-1
        for arr in accounts:
            max_= max(sum(arr),max_)

        return max_
        