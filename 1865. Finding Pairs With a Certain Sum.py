from collections import Counter
class FindSumPairs:


    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1=nums1
        self.nums2=nums2
        self.num2_freq = Counter(self.nums2)
        
        

    def add(self, index: int, val: int) -> None:
        if  self.num2_freq[self.nums2[index]] > 1:
            self.num2_freq[self.nums2[index]]-=1
        else:
            del self.num2_freq[self.nums2[index]]

        self.nums2[index]+=val
        self.num2_freq[self.nums2[index]]+=1

        

    def count(self, tot: int) -> int:
        count=0
        for element in self.nums1:
            if tot-element in self.num2_freq.keys():
                count+=self.num2_freq[tot-element]
        return count



        

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)