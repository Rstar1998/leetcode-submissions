# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr=head.next
        prev=head
        swap=1
        while curr:
            if swap ==1:
                temp = curr.val
                curr.val = prev.val
                prev.val = temp
                swap=0
            else:
                swap=1

            prev=curr
            curr=curr.next
        return head
            


            



        
        