class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print(intervals)
        count = 0
        prev_end = 0 
        
        for start, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end 
                
        return count
        