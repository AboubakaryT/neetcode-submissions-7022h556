# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        j = 0
        for i in range(len(lists)):
            while lists[i]:
                arr.append(lists[i].val)
                lists[i] = lists[i].next

        arr = sorted(arr)
        dummy = ListNode()
        if arr:
         head = ListNode(arr[0])
         dummy.next = head

        for i in range(1,len(arr)):
            head.next = ListNode(arr[i])
            head = head.next
        return dummy.next
            
