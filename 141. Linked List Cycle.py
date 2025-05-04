# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        sp=head
        fp=head.next

        while fp:
            if sp == fp:
                return True

            sp=sp.next
            
            if fp.next is None:
                return False
            fp=(fp.next).next
            

        