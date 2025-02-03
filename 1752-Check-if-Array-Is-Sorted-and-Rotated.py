class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if n ==1 :
            return True

        i=0
        count=0
      
        while i <= (2*len(nums))-2:
            if nums[i%n] <= nums[(i+1)%n]:
                count+=1
            else:
                count=0
            
            if count == (len(nums)-1):
                return True
            i+=1
        return False


        