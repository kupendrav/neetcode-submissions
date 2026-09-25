from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping of digits to letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Edge case: empty input
        if not digits:
            return []

        res = []

        # Backtracking function
        def backtrack(index: int, path: str):
            # Base case: if we've used all digits
            if index == len(digits):
                res.append(path)
                return

            # Get possible letters for current digit
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                # Add letter and move to next digit
                backtrack(index + 1, path + letter)

        # Start backtracking from index 0 with empty path
        backtrack(0, "")
        return res
