# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Dictionary to map original node -> cloned node
        cloned = {}

        def dfs(curr):
            # If already cloned, return it
            if curr in cloned:
                return cloned[curr]

            # Clone current node
            copy = Node(curr.val)
            cloned[curr] = copy

            # Clone neighbors recursively
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
