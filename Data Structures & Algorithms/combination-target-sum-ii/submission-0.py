from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to handle duplicates and enable pruning
        res = []

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                res.append(path[:])  # Found a valid combination
                return
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If current number exceeds remaining target, break (pruning)
                if candidates[i] > remaining:
                    break
                # Choose the current number
                path.append(candidates[i])
                # Move to next index (i+1) since each number can be used once
                backtrack(i + 1, path, remaining - candidates[i])
                # Undo the choice
                path.pop()

        backtrack(0, [], target)
        return res
