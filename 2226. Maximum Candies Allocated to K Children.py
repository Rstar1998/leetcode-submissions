class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        start=1
        end=max(candies)
        max_cnt = 0
        while start <= end:
            mid = (start+end)//2
            

            count=0

            if mid == 0:
                break

            for elm in candies:
                count+=elm//mid

            if count>=k:
                max_cnt=max(max_cnt,mid)
                start=mid+1
            else:
                end=mid-1


            
        return max_cnt
        