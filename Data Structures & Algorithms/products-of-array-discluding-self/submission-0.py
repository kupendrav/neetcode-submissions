class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n   # start with all 1s

        # Step 1: build prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Step 2: multiply with suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
        