class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Mapping of closing to opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # If it's an opening bracket
                stack.append(char)
            elif char in mapping:  # If it's a closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                # Invalid character (not a bracket)
                return False
        
        # If stack is empty, all brackets matched correctly
        return not stack
