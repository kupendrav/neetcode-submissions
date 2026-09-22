class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(current_string, open_count, close_count):
            # If the current string is of length 2 * n, we have a valid combination
            if len(current_string) == 2 * n:
                res.append(current_string)
                return
            
            # We can add an opening bracket if we haven't used all n of them
            if open_count < n:
                backtrack(current_string + '(', open_count + 1, close_count)
            
            # We can add a closing bracket if there are unclosed opening brackets
            if close_count < open_count:
                backtrack(current_string + ')', open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return res