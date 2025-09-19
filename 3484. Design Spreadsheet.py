class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.h = defaultdict(int)
        

    def setCell(self, cell: str, value: int) -> None:
        self.h[cell] = value
        

    def resetCell(self, cell: str) -> None:
        self.h[cell] = 0
        

    def getValue(self, formula: str) -> int:
        nums = formula.strip("=").split("+")
        a = nums[0]
        b = nums[1]
        if a.isdigit():
            a = int(a)
        elif a in self.h:
            a = self.h[a]
        else:
            a = 0

        if b.isdigit():
            b = int(b)
        elif b in self.h:
            b = self.h[b]
        else:
            b = 0
        
        return a+b

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)