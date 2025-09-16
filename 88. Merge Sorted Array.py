class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total = len(nums1)
        k = 0
        for i in range(n):
            if m < total:
                nums1[m] = nums2[k]
                t = m
                
                while t>0 and nums1[t] < nums1[t-1]:
                    
                    temp = nums1[t]
                    nums1[t] = nums1[t-1]
                    nums1[t-1] = temp
                    t-=1
                    
                m+=1
                k+=1
        return nums1





        