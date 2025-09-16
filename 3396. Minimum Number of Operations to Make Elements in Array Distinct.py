from collections import Counter, deque
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        f = Counter(nums)
        queue = deque(nums)
        count=0
        while max(f.values()) != 1:
            if len(queue)> 3:
                for i in range(3):
                    first  = queue.popleft()
                    f[first]-=1
                count+=1
            else:
                count+=1
                break
        return count
            
        