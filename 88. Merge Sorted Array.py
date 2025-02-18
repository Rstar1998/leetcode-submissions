class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=len(nums1)-n
        j=0
        while j <= n-1:
            nums1[i+j] = nums2[j]
            j+=1
        print(nums1)

        while i <= len(nums1)-1:
            
            c = i
            while c>0:
                if nums1[c-1]>nums1[c]:
                    nums1[c-1],nums1[c] = nums1[c],nums1[c-1]
                else:
                    break
                c-=1

            i+=1 
        return nums1
        
        