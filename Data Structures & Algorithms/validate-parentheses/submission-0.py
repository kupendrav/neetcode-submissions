class Solution:
    def isValid(self, s: str) -> bool:
        # Odd length strings can never be valid
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (ch == ')' and top != '(') or \
                   (ch == '}' and top != '{') or \
                   (ch == ']' and top != '['):
                    return False
        
        return not stack
