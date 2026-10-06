from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        def bfs(start_cells):
            visit = set(start_cells)
            queue = deque(start_cells)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit and heights[nr][nc] >= heights[r][c]:
                        visit.add((nr, nc))
                        queue.append((nr, nc))
            return visit

        pac_starts = []
        atl_starts = []
        
        # Collect Pacific (top and left) and Atlantic (bottom and right) borders
        for c in range(cols):
            pac_starts.append((0, c))
            atl_starts.append((rows - 1, c))
            
        for r in range(rows):
            pac_starts.append((r, 0))
            atl_starts.append((r, cols - 1))
            
        pac_reach = bfs(pac_starts)
        atl_reach = bfs(atl_starts)
        
        # Find cells present in both sets
        return list(map(list, pac_reach.intersection(atl_reach)))