class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        p1=0
        p2=0
        output=[]

        while ( (p1 < len(nums1)) and (p2 < len(nums2)) ):
            id1, val1 = nums1[p1]
            id2, val2 = nums2[p2]

            if  id1 == id2:
                output.append( [ id1 , val1+val2 ] )
                p1+=1
                p2+=1
            elif id1 < id2:
                output.append( [ id1 , val1 ] )
                p1+=1
            else:
                output.append( [ id2 , val2 ] )
                p2+=1

        while(p1 < len(nums1)):
            id1, val1 = nums1[p1]
            output.append( [ id1 , val1 ] )
            p1+=1

        while(p2 < len(nums2)):
            id2, val2 = nums2[p2]
            output.append( [ id2 , val2 ] )
            p2+=1   

        return output
        