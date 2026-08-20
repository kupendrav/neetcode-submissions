class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # Step 1: Clone nodes and interleave them. 
        # A -> B becomes A -> A' -> B -> B'
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next # Move to the next original node
            
        # Step 2: Assign random pointers for the copies.
        curr = head
        while curr:
            if curr.random:
                # The copy is curr.next. Its random should point to the copy of curr.random.
                curr.next.random = curr.random.next
            curr = curr.next.next # Jump to the next original node
            
        # Step 3: Separate the lists and restore the original list.
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next # Restore original list pointer
            if copy.next:
                copy.next = copy.next.next # Link the copied list together
            curr = curr.next
            
        return copy_head