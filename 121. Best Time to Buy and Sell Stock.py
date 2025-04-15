class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        current_min = prices[0]
        for i in range(1,len(prices)):
             current_min = min(current_min,prices[i])
             profit = max(profit , prices[i]-current_min )

        return profit


        
       
       
         