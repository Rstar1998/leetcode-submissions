from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_dict=defaultdict(set)

        ball_current_color = {}

        output=[]
        for row in queries:
            ball = row[0]
            color = row[1]
            if ball in ball_current_color:
                current_color = ball_current_color[ ball ]
                if len(ball_dict[current_color]) > 1:
                    ball_dict[current_color].remove(ball)
                else:
                    ball_dict.pop(current_color)
                

            ball_dict[color].add(ball)
            ball_current_color[ ball ] = color

            output.append(len(ball_dict))
        return output

     
    

 
        