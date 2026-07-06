from collections import defaultdict, deque
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the adjacency list for the graph
        graph = defaultdict(list)
        for u, v, distance in roads:
            graph[u].append((v, distance))
            graph[v].append((u, distance))
            
        # Step 2: Initialize BFS
        queue = deque([1])
        visited = set([1])
        min_score = float('inf')
        
        # Step 3: Traverse the connected component containing node 1
        while queue:
            node = queue.popleft()
            
            for neighbor, distance in graph[node]:
                # Update the minimum score with every edge we encounter
                min_score = min(min_score, distance)
                
                # If the neighbor hasn't been visited, add to queue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score