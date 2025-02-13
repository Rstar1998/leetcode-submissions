from sortedcontainers import SortedList
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        sr_l = SortedList(nums)
        cnt=0
        while len(sr_l) >= 2 and sr_l[0] < k :
            x = sr_l.pop(0)
            y = sr_l.pop(0)

            sr_l.add(min(x, y) * 2 + max(x, y))

            cnt+=1
        return cnt




        