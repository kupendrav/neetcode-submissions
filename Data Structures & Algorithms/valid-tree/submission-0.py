class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootX] = rootY
            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True
