#old 

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        arr=[0]
        max_ = max(nums)
        s=0
        for el in nums:
            if el >= max_:
                s+=1
            arr.append(s)

        
        count=0
        for left in range(1,len(arr)):
            right=len(arr)-1
            diff=arr[left-1]

            while right >= left:
                
                if arr[right]-diff >= k :
                    count+=1
                else:
                    break
                right-=1

        return count


 
############

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_el = max(nums)
        count = 0
        l = 0
        max_found = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == max_el:
                max_found += 1

            while max_found >= k:
                count += n - r
                if nums[l] == max_el:
                    max_found -= 1
                l += 1

        return count
       
        