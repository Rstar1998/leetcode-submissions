class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        mx = 0
        n = len(points)
        
        for p1 in range(n-2):  
            for p2 in range(p1+1, n-1):  
                for p3 in range(p2+1, n):  
                    
                    x1, y1 = points[p1]
                    x2, y2 = points[p2]
                    x3, y3 = points[p3]
                    
                    area = 1/2 * abs(
                        x1 * (y2 - y3) + 
                        x2 * (y3 - y1) + 
                        x3 * (y1 - y2)
                    )
                    
                    mx = max(mx, area)

        return mx
        