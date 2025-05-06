class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        frequencies = defaultdict(int)
    
        for row in matrix:
            pattern = ""
            
            for col in range(len(row)):
                if row[0] == row[col]:
                    pattern += "T"
                else:
                    pattern += "F"
            
            frequencies[pattern] += 1
        
        res = 0
        
        for count in frequencies.values():
            res = max(count, res)
        
        return res