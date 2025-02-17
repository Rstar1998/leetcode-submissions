class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        days = len(pizzas)//4
        pizzas.sort()
        
        weight=0
        d=1
        while d<=days:
            if d%2 == 1:
                v = pizzas.pop()
                weight+=v
            d+=1
        d=1
        while d<=days:
            if d%2 == 0:
                v1 = pizzas.pop()
                v2 = pizzas.pop()
                weight+=v2
            d+=1
        return weight
        


       