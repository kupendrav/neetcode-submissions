class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        nums.sort()  # Sorting helps prune invalid branches early

        def backtrack(start_idx: int, current_combo: list[int], remaining_target: int):
            if remaining_target == 0:
                res.append(list(current_combo))
                return

            for i in range(start_idx, len(nums)):
                # Early stopping: since nums is sorted, subsequent numbers will also exceed remaining_target
                if nums[i] > remaining_target:
                    break

                current_combo.append(nums[i])
                # Pass 'i' instead of 'i + 1' to allow reusing the same element
                backtrack(i, current_combo, remaining_target - nums[i])
                current_combo.pop()  # Backtrack

        backtrack(0, [], target)
        return res