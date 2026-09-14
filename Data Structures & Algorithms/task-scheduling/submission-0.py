from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequencies of tasks
        freq_map = Counter(tasks)
        
        # Step 2: Find the maximum frequency
        max_freq = max(freq_map.values())
        
        # Step 3: Count how many tasks have this maximum frequency
        count_max = sum(1 for v in freq_map.values() if v == max_freq)
        
        # Step 4: Apply the formula
        part_count = (max_freq - 1) * (n + 1) + count_max
        
        # Step 5: Return the maximum between formula result and total tasks
        return max(part_count, len(tasks))
