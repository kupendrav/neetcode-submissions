class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: frequency map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Step 2: buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Step 3: collect top k
        result = []
        for freq in range(len(buckets) - 1, 0, -1):  # from n down to 1
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
