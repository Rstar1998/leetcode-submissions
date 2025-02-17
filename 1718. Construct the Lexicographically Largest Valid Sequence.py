class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        used = set()
        output_str = [0] * ((2*n)-1)

        def backtrack(index,used,output_str):

            if index == len(output_str):
                return True

            if output_str[index]!=0:
                return backtrack(index+1,used,output_str)

            for i in range(n,0,-1):
                next_idx = index if i == 1 else index+i
                if (i in used ) or (next_idx >= len(output_str)) or ( output_str[next_idx] != 0):
                    continue
                 
                used.add(i)
                output_str[index]=i
                output_str[next_idx]=i

                if backtrack(index+1,used,output_str):
                    return True

                used.remove(i)
                output_str[index]=0
                output_str[next_idx]=0

            return False

                    

        backtrack(0,used,output_str)
        return output_str

      
        




        

       
        
         
    


        