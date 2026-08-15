# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # Step 1: Save next
            curr.next = prev        # Step 2: Reverse pointer
            prev = curr             # Step 3: Move prev forward
            curr = next_node        # Step 4: Move curr forward

        return prev  # New head
