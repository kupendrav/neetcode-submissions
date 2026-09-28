class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the full word when a word ends at this node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        # 2. Backtracking DFS function
        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent.children[char]

            # Check if we matched a full word
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Prevent adding duplicate words

            # Mark cell as visited
            board[r][c] = '#'

            # Explore 4 directional neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            # Backtrack: Restore original character
            board[r][c] = char

            # Optimization: Prune Trie leaf nodes that no longer lead to words
            if not curr_node.children:
                del parent.children[char]

        # 3. Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result