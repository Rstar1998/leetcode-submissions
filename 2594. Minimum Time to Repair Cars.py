import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        start=min(ranks)

        end = max(ranks) * cars * cars

        def valid_time(ranks, time, cars):
            t=0

            for i in ranks:
                t += math.floor(math.sqrt(time / i ))
                if t >= cars:
                    return True
            return False
            

        min_time=0

        while start <= end:
            mid = start + ((end-start)//2)

            if valid_time(ranks, mid, cars):
                end = mid-1
                min_time=mid
            else:
                start = mid+1

        return min_time






        