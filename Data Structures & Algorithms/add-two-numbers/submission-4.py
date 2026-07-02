# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        res = ListNode(0)
        head = res
        while l1 or l2 or carry:
            num1 = 0
            num2 = 0 
            if l1:
                num1 = l1.val
                l1 = l1.next
            if l2:
                num2 = l2.val
                l2 = l2.next

            total = num1 + num2 + carry
            carry = total // 10
            digit = total % 10
            res.next = ListNode(digit)
            res = res.next
            
        return head.next



