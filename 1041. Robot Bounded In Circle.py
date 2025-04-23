class Solution:
    def isRobotBounded(self, instructions: str) -> bool:

        di ="N"
        x=0
        y=0
        for i in instructions:
            if i == "L":
                if di == "N":
                    di="W"
                elif di == "W":
                    di="S"
                elif di == "E":
                    di ="N"
                else:
                    di="E"
            elif i == "R":
                if di == "N":
                    di="E"
                elif di == "W":
                    di="N"
                elif di == "E":
                    di ="S"
                else:
                    di="W"
            else:
                if di == "N":
                    y+=1
                elif di == "W":
                    x-=1
                elif di == "E":
                    x+=1
                else:
                    y-=1
        
        if x==0 and y ==0:
            return True

        if di == "N":
            return False

        return True
        

            

        