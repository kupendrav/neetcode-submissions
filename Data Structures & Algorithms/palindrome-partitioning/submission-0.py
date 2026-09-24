class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int, path: list[str]):
            # Base case: if we reach the end of the string, add the path to results
            if start == len(s):
                res.append(list(path))
                return
            
            # Try every possible ending position for the current substring
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end + 1, path)
                    path.pop() # Backtrack
                    
        backtrack(0, [])
        return res