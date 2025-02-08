from collections import defaultdict
from sortedcontainers import SortedSet
import heapq
class NumberContainers:
    

    def __init__(self):
        self.number_index={}
        self.small_index=defaultdict(SortedSet)
        

    def change(self, index: int, number: int) -> None:
        if number in self.small_index  :     
            self.small_index[number].discard(index)

        if index in self.number_index:
            self.small_index[self.number_index[index]].discard(index)
    
        self.small_index[number].add(index)

        self.number_index[index] = number
        
            
    
    def find(self, number: int) -> int:
        if len(self.small_index[number]) == 0:
            return -1
        else:
            return self.small_index[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)