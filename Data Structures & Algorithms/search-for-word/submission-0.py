class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(r: int, c: int, i: int) -> bool:
            # Base case: All characters found
            if i == len(word):
                return True
            
            # Check bounds and character match
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                board[r][c] != word[i]):
                return False
            
            # Mark the current cell as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 neighboring directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            
            # Unmark (backtrack)
            board[r][c] = temp
            return found

        # Start DFS from every cell on the board
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
                    
        return False