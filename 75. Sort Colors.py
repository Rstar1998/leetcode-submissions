# dutch national flag sorting
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red=0
        blue=len(nums)-1
        i=0
        while  i<= blue:
            if nums[i] == 0:
                temp=nums[red]
                nums[red]=nums[i]
                nums[i]=temp
                i+=1
                red+=1
            elif nums[i] ==1:
                i+=1
            else:
                nums[i] , nums[blue] = nums[blue] , nums[i]
                blue-=1
        


