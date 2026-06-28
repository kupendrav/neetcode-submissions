class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[num] = i
        return []
        