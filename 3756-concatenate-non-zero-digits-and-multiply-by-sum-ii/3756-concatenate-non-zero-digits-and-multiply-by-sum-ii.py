class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        n = len(s)
        
        # Precompute powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        sumD = [0] * (n + 1)
        cntN0 = [0] * (n + 1)
        p = [0] * (n + 1)
        
        # Build prefix arrays
        for i in range(n):
            d = int(s[i])
            sumD[i + 1] = sumD[i] + d
            cntN0[i + 1] = cntN0[i] + (1 if d > 0 else 0)
            p[i + 1] = (p[i] * 10 + d) % MOD if d > 0 else p[i]
            
        ans = []
        # Answer each query in O(1)
        for l, r in queries:
            n0 = cntN0[r + 1] - cntN0[l]
            sd = sumD[r + 1] - sumD[l]
            x = (p[r + 1] - p[l] * pow10[n0]) % MOD
            ans.append((x * sd) % MOD)
            
        return ans