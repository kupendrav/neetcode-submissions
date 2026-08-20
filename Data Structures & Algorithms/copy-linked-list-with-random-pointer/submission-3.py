class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mp = {None: None}
        curr = head
        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            cp = mp[curr]
            cp.next = mp[curr.next]
            cp.random = mp[curr.random]
            curr = curr.next
        return mp[head]