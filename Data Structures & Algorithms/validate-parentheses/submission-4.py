class Solution:
    def isValid(self, s: str) -> bool:
        # Odd length strings can never be valid
        if len(s) % 2 != 0:
            return False

        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (c == ')' and top != '(') or \
                   (c == ']' and top != '[') or \
                   (c == '}' and top != '{'):
                    return False

        return not stack
