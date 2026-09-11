import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert to max-heap by negating values
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = -heapq.heappop(stones)  # heaviest
            x = -heapq.heappop(stones)  # second heaviest
            
            if y != x:
                heapq.heappush(stones, -(y - x))
        
        return -stones[0] if stones else 0
