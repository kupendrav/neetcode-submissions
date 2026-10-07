from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "S"  # Mark as safe
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Step 1: Mark border-connected 'O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)
        
        # Step 2: Flip captured regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"  # Captured
                elif board[r][c] == "S":
                    board[r][c] = "O"  # Restore safe
