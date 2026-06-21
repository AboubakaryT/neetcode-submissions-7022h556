# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm = {}
        while head:
            hm[head] = 1 + hm.get(head, 0)
            if hm[head] >= 2:
                return True
            head = head.next
        return False