from typing import List
from collections import deque
import math

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        
        # 1. Build adjacency list and compute in-degrees for the entire graph
        for u, v, w in edges:
            adj[u].append((v, w))
            in_degree[v] += 1
            
        # 2. Find Topological Order using Kahn's Algorithm
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        topo = []
        
        while queue:
            u = queue.popleft()
            topo.append(u)
            for v, w in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        # 3. Helper function to check if a valid path exists for a given minimum edge-cost requirement (mid)
        def check(mid: int) -> bool:
            dist = [math.inf] * n
            dist[0] = 0
            
            # Process nodes in topological order to find the shortest path
            for u in topo:
                # If node is unreachable or offline, skip it
                if dist[u] == math.inf or not online[u]:
                    continue
                
                for v, w in adj[u]:
                    # Ignore offline destinations and edges that don't meet our 'mid' criteria
                    if not online[v]:
                        continue
                    if w >= mid:
                        if dist[u] + w < dist[v]:
                            dist[v] = dist[u] + w
                            
            return dist[n - 1] <= k

        # 4. Binary search for the maximum valid minimum edge-cost
        left, right = 0, 10**9
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid        # This mid is feasible, try for a higher minimum
                left = mid + 1
            else:
                right = mid - 1  # This mid is too high, lower the minimum requirement
                
        return ans