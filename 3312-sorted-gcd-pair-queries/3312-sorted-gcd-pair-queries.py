from collections import Counter
import itertools
import bisect

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_num = max(nums)
        
        freq = Counter(nums)
        
        count_divisors = [0] * (max_num + 1)
        for d in range(1, max_num + 1):
            for multiple in range(d, max_num + 1, d):
                count_divisors[d] += freq[multiple]
                
        count_gcd = [0] * (max_num + 1)
        for g in range(max_num, 0, -1):
            v = count_divisors[g]
            total_pairs = v * (v - 1) // 2
            
            for larger_g in range(2 * g, max_num + 1, g):
                total_pairs -= count_gcd[larger_g]
                
            count_gcd[g] = total_pairs
            
        prefix_sums = list(itertools.accumulate(count_gcd))
        
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans