from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r: int, c: int):
            # Base cases: out of bounds or cell is water ('0')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Mark cell as visited by sinking it to '0'
            grid[r][c] = '0'
            
            # Traverse adjacent neighbors (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Iterate through every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)  # Sink the entire island

        return island_count