class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        print(points)
        points.sort(key=lambda x: (-x[0], x[1]))
        print(points)
       
        cnt = 0
        for i in range(len(points) - 1):
            x, y = points[i]
            high = 1<<31
            for j in range(i + 1, len(points)):
                if high > points[j][1] >= y:
                    cnt += 1
                    high = points[j][1]
                    if high == y: break
        return cnt