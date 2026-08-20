"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary to map original nodes to their copies. 
        # Mapping None to None handles edge cases for the tails and null random pointers automatically.
        oldToCopy = {None: None}
        
        # First Pass: Create a copy of every single node and store it in the hash map.
        curr = head
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
            
        # Second Pass: Link the next and random pointers of the copied nodes.
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
            
        # Return the head of our newly copied list
        return oldToCopy[head]