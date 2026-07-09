class Solution:

    def reverseKList(self, node, k):

        counter = node
        count = 0

        while counter:
            count += 1
            counter = counter.next

        cycles = count // k

        prev = None
        currHead = None
        dummy = None
        groupStart = node

        i = 0
        groups = 0

        while node and groups < cycles:
            curr = node.next
            node.next = prev
            prev = node
            node = curr
            i += 1

            if i == k:

                groups += 1

                if currHead is None:
                    currHead = prev

                if dummy:
                    dummy.next = prev

                dummy = groupStart

                dummy.next = curr

                groupStart = curr
                prev = None
                i = 0

        return currHead

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.reverseKList(head, k)