class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections = []  # to store all intersecting intervals
        # index "i" to iterate over the length of list a and index "j"
        # to iterate over the length of list b
        i = j = 0

        # while loop will break whenever either of the lists ends
        while i < len(firstList) and j < len(secondList):
            # Let's check if interval_list_a[i] intersects interval_list_b[j]
            #  1. start - the potential startpoint of the intersection
            #  2. end - the potential endpoint of the intersection
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:    # if this is an actual intersection
                intersections.append([start, end])   # add it to the list

            # Move forward in the list whose interval ends earlier
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections
        