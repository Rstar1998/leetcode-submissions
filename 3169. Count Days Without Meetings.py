class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)       
        last = 1
        count=0

        for ind , intv in enumerate(meetings):
            start = intv[0]
            end = intv[1]
            if last < start:
                if ind == 0:
                    count+= (start-last)
                else:
                    count+= (start-last-1)

            last = max(last,end)
         

        if last != days:
            count+= (days-last)

        return count

 