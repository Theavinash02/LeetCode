from typing import List
import math

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        sorted_nodes = sorted((num, i) for i, num in enumerate(nums))
        sorted_nums = [x for x, _ in sorted_nodes]

        pos = {}
        for i, (_, idx) in enumerate(sorted_nodes):
            pos[idx] = i

        LOG = n.bit_length() + 1
        jump = [[0] * LOG for _ in range(n)]

        r = 0
        for l in range(n):
            while r + 1 < n and sorted_nums[r + 1] - sorted_nums[l] <= maxDiff:
                r += 1
            jump[l][0] = r

        for k in range(1, LOG):
            for i in range(n):
                jump[i][k] = jump[jump[i][k - 1]][k - 1]

        def solve(l, r, k):
            if l == r:
                return 0
            if jump[l][0] >= r:
                return 1
            if jump[l][k] < r:
                return math.inf

            while k >= 0 and jump[l][k] >= r:
                k -= 1

            return (1 << k) + solve(jump[l][k], r, k)

        ans = []

        for u, v in queries:
            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            d = solve(l, r, LOG - 1)
            ans.append(-1 if d == math.inf else d)

        return ans