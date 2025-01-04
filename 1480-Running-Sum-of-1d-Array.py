class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 1 or size == 0:
            return nums

        runningSum = [0] * size
        runningSum[0] = nums[0]

        for i in range(1, size):
            runningSum[i] = nums[i] + runningSum[i - 1]

        return runningSum
