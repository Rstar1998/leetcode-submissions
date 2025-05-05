import heapq
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []
        taken = set()
        
        for index in range(len(nums)):
            if nums[index] in taken:
                continue
            
            if len(heap) == 3:
                if heap[0] < nums[index]:
                    taken.remove(heap[0])
                    heapq.heappop(heap)
                    
                    heapq.heappush(heap, nums[index])
                    taken.add(nums[index])
                    
            else:
                heapq.heappush(heap, nums[index])
                taken.add(nums[index])
        
        if len(heap) == 1:
            return heap[0]
        
        elif len(heap) == 2:
            first_num = heap[0]
            heapq.heappop(heap)
            return max(first_num, heap[0])
        
        return heap[0]



        