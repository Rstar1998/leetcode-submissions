from collections import defaultdict,deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph=defaultdict(set)
        indegree = defaultdict(int)

        for re,ing in zip(recipes,ingredients):
            for i in ing:
                graph[i].add(re)
                indegree[re]+=1
        
        ans=[]
        recp = set(recipes)
        queue = deque(supplies)
        while queue:
            ele = queue.popleft()
            if ele in recp:
                ans.append(ele)
            for con in graph[ele]:
                indegree[con]-=1
                if indegree[con] == 0:
                    queue.append(con)
        return ans
                    






        