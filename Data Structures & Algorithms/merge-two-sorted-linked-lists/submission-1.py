# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterate throughout the longest linkedList
        and we compare values.  
        """
        res = ListNode()
        head = res
        while list1 and list2:
            if list1.val >= list2.val:
                res.next = list2
                res = res.next
                list2 = list2.next
            else:
                res.next = list1 
                res = res.next 
                list1 = list1.next

           
        while list1:
            res.next = list1
            res = res.next
            list1 = list1.next
        
        while list2:
            res.next = list2
            res = res.next
            list2= list2.next
        return head.next
        