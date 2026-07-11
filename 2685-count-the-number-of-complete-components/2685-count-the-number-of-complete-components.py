from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            nodes = 1
            degree_sum = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    c_nodes, c_degree = dfs(nei)
                    nodes += c_nodes
                    degree_sum += c_degree

            return nodes, degree_sum

        ans = 0

        for i in range(n):
            if not visited[i]:
                nodes, degree_sum = dfs(i)

                # degree_sum counts every edge twice
                edges_in_component = degree_sum // 2

                if edges_in_component == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans