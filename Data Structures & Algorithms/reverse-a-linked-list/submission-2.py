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
            # Step 1: Save next node
            next_node = curr.next

            # Step 2: Reverse the pointer
            curr.next = prev

            # Step 3: Advance prev and curr
            prev = curr
            curr = next_node

        # prev is the new head
        return prev
