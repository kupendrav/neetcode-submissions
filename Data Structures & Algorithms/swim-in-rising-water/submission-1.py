from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        
        # Min-heap: (elevation, row, col)
        heap = [(grid[0][0], 0, 0)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            elevation, r, c = heapq.heappop(heap)
            
            # If we reached destination, return elevation
            if r == n-1 and c == n-1:
                return elevation
            
            if visited[r][c]:
                continue
            visited[r][c] = True
            
            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    # Max elevation along the path
                    heapq.heappush(heap, (max(elevation, grid[nr][nc]), nr, nc))
