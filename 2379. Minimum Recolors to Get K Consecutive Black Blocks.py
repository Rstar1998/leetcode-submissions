class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        temp = "N"+blocks

        count = [0]*len(temp)
        w_count =0
        min_value = float("inf")

        for i in range(1,len(temp)):
            if blocks[i-1] == "W":
                w_count+=1
            count[i] = w_count
        
        i=0 
        while i < (len(count)-k):
            print(i+k)
            no_w = count[i+k]-count[i]
            min_value=min(min_value,no_w)
            i+=1
        return min_value


    
