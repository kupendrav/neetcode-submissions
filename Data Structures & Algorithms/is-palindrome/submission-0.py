class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Normalize the string
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        
        # Step 2: Two-pointer check
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        
        # Step 3: If all matched
        return True
