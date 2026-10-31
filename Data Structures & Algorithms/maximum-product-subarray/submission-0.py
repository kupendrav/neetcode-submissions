class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = ans = nums[0]

        for num in nums[1:]:
            temp_max = max(
                num,
                num * max_prod,
                num * min_prod
            )

            temp_min = min(
                num,
                num * max_prod,
                num * min_prod
            )

            max_prod = temp_max
            min_prod = temp_min

            ans = max(ans, max_prod)

        return ans