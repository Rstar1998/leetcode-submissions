# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        if head.next is None:
            return head

        new_head=None

        def recursive(current):
            nonlocal new_head
            if current.next is None:
                
                new_head = current

                return current
            
            post_curr = recursive(current.next)
            current.next=None
            post_curr.next=current
            return current

        recursive(head)
        return new_head