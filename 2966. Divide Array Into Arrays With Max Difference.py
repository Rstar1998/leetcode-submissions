class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        output = []

        nums.sort()

        i=0

        while i+3 <= len(nums):
            temp = nums[i:i+3]
            if temp[-1]-temp[0] <= k:
                output.append(temp)
            else:
                return []
            i+=3
        return output



  
        