# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head

        temp=head
        length=0
        while temp.next:
            length+=1
            temp = temp.next

        length+=1

        
        k = k % length
        

        while k>0:

            temp_head=head
            curr=head
            prev=None
            while curr.next:
                prev=curr
                curr=curr.next
            prev.next=None
            curr.next=temp_head
            head=curr
            k-=1
        return head
        