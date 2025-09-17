class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        h={ a : False for a in nums}
        m = 0
        for ele in nums:
            if not h[ele]:
                fc=0
                bc=0
                fp = ele
                bp = ele-1

                while fp in h:
                    h[fp] = True
                    fp+=1
                    fc+=1
                
                while bp in h:
                    h[bp] = True
                    bp-=1
                    bc+=1
                m = max(m,fc+bc)
        return m

        