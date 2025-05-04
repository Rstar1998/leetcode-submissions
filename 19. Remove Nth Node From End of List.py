# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next is None and n==1:
            return None

        k=1
        first=head
        while k<=n:
            first=first.next
            k+=1
        
        second=head

        if first is None:
            head=head.next
            second.next=None
            return head

        while first.next:
            first=first.next
            second=second.next
        
        post=second.next
        second.next=post.next
        post.next=None

    
        return head



        