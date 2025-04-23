class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        out=[]
        prev = intervals[0]
        for i,curr in enumerate(intervals[1:]):
            if curr[0] <= prev[1]:
                prev[1] = max(curr[1],prev[1])
                continue
            else:
                out.append([ prev[0], prev[1] ] )
                prev = curr
        
    
        out.append([ prev[0], prev[1] ] )
        return out
            



        