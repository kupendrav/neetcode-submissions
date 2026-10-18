from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Build graph and indegree map
        graph = defaultdict(set)
        indegree = {}
        
        # Initialize indegree for all unique characters
        for word in words:
            for char in word:
                indegree[char] = 0
        
        # Step 2: Build edges by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            
            # Invalid case: prefix issue
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            
            # Find first differing character
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    break
        
        # Step 3: Topological sort using queue
        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []
        
        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: Check for cycle
        if len(result) < len(indegree):
            return ""
        
        return "".join(result)
