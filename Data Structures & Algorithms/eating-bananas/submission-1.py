class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper function to calculate hours needed at speed k
        def can_finish(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        # Binary search boundaries
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                result = mid
                right = mid - 1  # try smaller k
            else:
                left = mid + 1  # need larger k

        return result
