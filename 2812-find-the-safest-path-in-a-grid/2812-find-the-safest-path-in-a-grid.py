from typing import List
from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        Find the maximum safeness factor of all paths from (0,0) to (n-1, n-1).
        Safeness factor = minimum Manhattan distance to any thief along the path.
        
        Time: O(n² log n)
        Space: O(n²)
        """
        n = len(grid)
        
        # Edge case: if start or end contains a thief, answer is 0
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        
        # Phase 1: Multi-source BFS to compute distance to nearest thief
        dist = self._compute_distances(grid, n)
        
        # Phase 2: Modified Dijkstra to find path maximizing minimum distance
        return self._find_max_safeness_path(dist, n)
    
    def _compute_distances(self, grid: List[List[int]], n: int) -> List[List[int]]:
        """Phase 1: Multi-source BFS from all thief positions."""
        dist = [[-1] * n for _ in range(n)]
        queue = deque()
        
        # Enqueue all thief positions with distance 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    dist[r][c] = 0
        
        # BFS: expand outward from all thieves level-by-level
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        return dist
    
    def _find_max_safeness_path(self, dist: List[List[int]], n: int) -> int:
        """Phase 2: Modified Dijkstra with max-heap for bottleneck optimization."""
        heap = [(-dist[0][0], 0, 0)]  # (negative_safeness, row, col)
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while heap:
            neg_safeness, r, c = heapq.heappop(heap)
            safeness = -neg_safeness
            
            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            # First arrival at destination is optimal
            if r == n - 1 and c == n - 1:
                return safeness
            
            # Explore neighbors: new safeness = min(current, neighbor's distance)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_safeness = min(safeness, dist[nr][nc])
                    heapq.heappush(heap, (-new_safeness, nr, nc))
        
        return 0