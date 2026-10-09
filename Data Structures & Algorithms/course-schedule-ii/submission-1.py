from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited
        order = []
        
        def dfs(course):
            if visited[course] == 1:  # cycle detected
                return False
            if visited[course] == 2:  # already processed
                return True
            
            visited[course] = 1  # mark as visiting
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 2  # mark as visited
            order.append(course)
            return True
        
        for c in range(numCourses):
            if visited[c] == 0:
                if not dfs(c):
                    return []
        
        return order[::-1]  # reverse to get correct order
