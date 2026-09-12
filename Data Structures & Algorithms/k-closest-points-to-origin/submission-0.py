import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use heapq.nsmallest to get k points with smallest distance
        return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
