from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Step 2: Min-heap (cost, node, stops)
        heap = [(0, src, 0)]
        
        # Step 3: Track best cost with stops
        dist = {(src, 0): 0}
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            # If destination reached
            if node == dst:
                return cost
            
            # If stops exceed limit, skip
            if stops > k:
                continue
            
            # Expand neighbors
            for nei, price in graph[node]:
                new_cost = cost + price
                if (nei, stops+1) not in dist or new_cost < dist[(nei, stops+1)]:
                    dist[(nei, stops+1)] = new_cost
                    heapq.heappush(heap, (new_cost, nei, stops+1))
        
        return -1
