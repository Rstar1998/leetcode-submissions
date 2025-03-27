class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def merge_rect(rectangles, dir):
            intv=[]
            for elm in rectangles:
                if dir:
                    intv.append((elm[0],elm[2])) # vertical
                else:
                    intv.append((elm[1],elm[3])) #horizontal

            intv= sorted(intv)
            merge = []

            curr = intv[0]
            for i in range(1,len(intv)):
                nxt = intv[i]

                if nxt[0] < curr[1] :
                    curr = ( curr[0] ,max( curr[1] , nxt[1] ) )
                else:
                    merge.append(curr)
                    curr = nxt
            merge.append(curr)
            return merge

        vert = merge_rect(rectangles, True)
        if len(vert) >= 3:
            return True
        
        hort = merge_rect(rectangles, False)
        if len(hort) >= 3:
            return True
        else:
            return False
        