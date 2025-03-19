class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def can_transform(nums,queries,k):
            diff_arr = [0]*(len(nums)+1)
            i=0
            while i < k:
                start= queries[i][0] 
                end= queries[i][1]+1
                diff_arr[start] += queries[i][2]
                diff_arr[end] -= queries[i][2]
                i+=1
            
            pre_sum=0
            for j in range(len(nums)):
                pre_sum+=diff_arr[j]
                if pre_sum < nums[j]:
                    return False
            return True


        start = 0
        end = len(queries)

        if not can_transform(nums,queries,end):
            return -1

        while start <= end:
            mid = start + ((end-start)//2)

            if can_transform(nums,queries,mid):
                end= mid-1
            else:
                start=mid+1
        
        return start


        