# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        sp = head
        fp = head

        while fp.next:
            sp=sp.next
            if fp.next is None:
                break
            fp = (fp.next).next
            if fp is None:
                break
        
        return sp

        