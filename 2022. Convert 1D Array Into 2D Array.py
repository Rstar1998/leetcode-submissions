class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        mat=[]
        start=0
        end = start+n
        if m*n != len(original):
            return []
        while end <= len(original):
            temp=original[start:end]
            print(temp)
            mat.append(temp.copy())
            start=end
            end = start+n
     
        return mat


