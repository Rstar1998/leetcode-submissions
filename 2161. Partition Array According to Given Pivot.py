class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before=[]
        equal=[]
        after=[]

        for i in nums:
            if i ==pivot:
                equal.append(i)
            elif i < pivot:
                before.append(i)
            else:
                after.append(i)
        return before + equal + after

        
        