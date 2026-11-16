class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        count = 0

        # Check whether k nodes exist
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        # Reverse k nodes
        prev = None
        curr = head

        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Connect with remaining list
        head.next = self.reverseKGroup(curr, k)

        return prev