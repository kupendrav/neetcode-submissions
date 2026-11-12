from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()   # stores indices
        res = []

        for i in range(len(nums)):
            # Remove indices outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Maintain decreasing order
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Record answer once first window is formed
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res