from collections import deque
from math import inf

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = grid[0][0]          # cost of standing on the start cell
        dq = deque([(0, 0)])

        while dq:
            x, y = dq.popleft()
            for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nd = dist[x][y] + grid[nx][ny]
                    if nd < dist[nx][ny]:
                        dist[nx][ny] = nd
                        if grid[nx][ny] == 1:
                            dq.append((nx, ny))       # cost-1 edge → back
                        else:
                            dq.appendleft((nx, ny))   # cost-0 edge → back... front!

        return dist[m - 1][n - 1] < health