class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        ps=-1
        ne=0
        out =[]
        for i in range(len(nums)):
            if nums[i] > -1:
                ps=i
                break
        
        if ps == -1:
            ps = len(nums)
            ne = len(nums)-1
        else:
            ne = ps-1
        
        print(ne,ps)

        while ne >= 0 and ps < len(nums):
            pss = nums[ps] * nums[ps]
            nes = nums[ne] * nums[ne]
            if pss < nes:
                out.append(pss)
                ps+=1
            elif pss > nes:
                out.append(nes)
                ne-=1
            else:
                out.append(pss)
                out.append(nes)
                ps+=1
                ne-=1

        while ne>=0:
            out.append(nums[ne] * nums[ne])
            ne-=1
        
        while ps < len(nums):
            out.append(nums[ps] * nums[ps])
            ps+=1
        
        return out



        