from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # will store indices of days
        
        for i in range(n - 1, -1, -1):  # traverse backwards
            # Pop all days that are not warmer than current day
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            # If stack not empty, next warmer day is at stack[-1]
            if stack:
                result[i] = stack[-1] - i
            
            # Push current day index
            stack.append(i)
        
        return result
