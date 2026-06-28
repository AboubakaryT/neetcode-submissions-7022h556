# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #0 -> 1 -> 2 -> 3 -> 4 -> 5 
        #0 -> 5 -> 1 -> 4 -> 2 -> 3

        fast = head
        slow = head
        dummy = ListNode()
        dummy.next = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        slowHead = ListNode()
        slowHead.next = slow
        while slow:
            #0 -> 1 -> 2
            #2 -> 1 -> 0
            #  0 -> None
            #keep track
            curr = slow.next
            slow.next = prev
            prev = slow
            slow = curr
        
        while head and prev and head.next and prev.next:
              headNext = head.next
              prevNext = prev.next
              head.next = prev
              prev.next = headNext
              head = headNext
              prev = prevNext
              #2,4
              #10,8,6
              #2 -> 10
            


            
    
        