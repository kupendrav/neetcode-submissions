class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)

        def backtrack(path):
            # Base case: full permutation
            if len(path) == len(nums):
                result.append(path[:])  # make a copy
                return

            # Try each unused number
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    backtrack(path)

                    # Backtrack step
                    path.pop()
                    used[i] = False

        backtrack([])
        return result
