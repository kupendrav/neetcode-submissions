from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        m, n = len(grid), len(grid[0])
        q = deque()
        
        # Step 1: Add all treasure chests (0) to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        # Step 2: BFS from all treasures simultaneously
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check bounds and if it's a land cell (INF)
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 2147483647:
                    grid[nx][ny] = grid[x][y] + 1
                    q.append((nx, ny))

