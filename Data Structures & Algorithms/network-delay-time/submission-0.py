from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Step 2: Min-heap for Dijkstra
        min_heap = [(0, k)]  # (time, node)
        dist = {}  # shortest time to each node
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node] = time
            for nei, wt in graph[node]:
                if nei not in dist:
                    heapq.heappush(min_heap, (time + wt, nei))
        
        # Step 3: Check if all nodes are reached
        if len(dist) == n:
            return max(dist.values())
        return -1
