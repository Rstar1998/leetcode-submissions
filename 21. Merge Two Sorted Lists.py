# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None :
            return None
        
        if list1 is None :
            return list2
        
        if list2 is None :
            return list1

        head=None
        tail=None

        while list1 and list2:
            if list1.val <= list2.val:
                temp=list1.next
                list1.next=None
                if head is None and tail is None:
                   
                    head=list1
                    tail=list1
                else:
                    
                    tail.next = list1
                    tail=tail.next
                list1=temp
            else:
                temp=list2.next
                list2.next=None
                if head is None and tail is None:
                    
                    head=list2
                    tail=list2
                else:
                    tail.next = list2
                    tail=tail.next
                list2=temp
        
        while list1 is not None:
            temp=list1.next
            list1.next=None
            tail.next = list1
            tail=tail.next
            list1=temp
        
        while list2 is not None:
            temp=list2.next
            list2.next=None
            tail.next = list2
            tail=tail.next
            list2=temp

        return head








        
        



       
        