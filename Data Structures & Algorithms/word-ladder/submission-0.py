from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Preprocess wordList into dictionary of generic states
        adj = defaultdict(list)
        L = len(beginWord)
        
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        # BFS
        queue = deque([(beginWord, 1)])  # (word, steps)
        visited = set([beginWord])
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                for nei in adj[pattern]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append((nei, steps + 1))
        
        return 0
