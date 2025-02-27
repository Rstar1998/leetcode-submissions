class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)

        maxcount = 0

        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                temp=[]
                temp.append(arr[i])
                temp.append(arr[j])
                for k in range(j+1,len(arr)):
                    if temp[-1]+temp[-2] in s:
                        temp.append(temp[-1]+temp[-2])
                    else:
                        break
                maxcount = max(maxcount,len(temp))
        return 0 if maxcount < 3 else maxcount


        