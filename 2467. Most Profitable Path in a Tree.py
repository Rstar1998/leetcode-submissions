from collections import defaultdict
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        bob_path=[]
        curr_path=[]

        aj_mat= defaultdict(set)
        for tu in edges:
            aj_mat[tu[0]].add(tu[1])
            aj_mat[tu[1]].add(tu[0])

        def dfs_get_bob_path(node,parent,curr_path,bob_path):
            if node == 0:
                bob_path.extend(curr_path)
                print(curr_path)
                print(bob_path)
                return True

            curr_path.append(node)

            for neigh in aj_mat[node]:
                if neigh!= parent and dfs_get_bob_path(neigh,node,curr_path,bob_path):
                    return True
                    
            curr_path.pop()
            return False


        dfs_get_bob_path(bob,-1,curr_path,bob_path)
        
        print(bob_path)
       
        size = len(bob_path)
        i=0
        while i < size//2:
            amount[bob_path[i]] = 0
            i+=1
        
        
        if (size+1)%2 == 0:
            amount[bob_path[i]] = 0
        else:
            amount[bob_path[i]]//= 2


        def alice_dfs(node,parent):
            value = float('-inf')

            for neig in aj_mat[node]:
                if neig!= parent:
                    value = max(value, alice_dfs(neig,node) + amount[node] )
        
            return amount[node] if value == float('-inf') else value

        return alice_dfs(0,-1)
       

        



    

        