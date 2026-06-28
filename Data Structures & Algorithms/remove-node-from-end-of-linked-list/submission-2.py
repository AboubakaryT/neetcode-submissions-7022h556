# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         dummy = ListNode()
         dummy.next = head

         first = head
         second = ListNode()
         second.next = head
         count = 0
         while first:
            first = first.next
            count+=1
            if count == n:
                break

         while first:
            second = second.next
            first = first.next
         if second.next == head:
            return second.next.next
         else:
            second.next = second.next.next

         return head
    


         