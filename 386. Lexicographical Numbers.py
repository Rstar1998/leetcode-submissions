from sortedcontainers import SortedList

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        # li = SortedList([])
        # for i in range(1,n+1):
        #     li.add(str(i))

        # return [ int(i) for i in li]

        ans=[]

        def dfs(ans,i,n):
            if i > n:
                return 
            ans.append(i)
            for k in range(0,10):
                dfs(ans,i*10+k,n)


        for i in range(1,10):
            dfs(ans,i,n)
        return ans


        

