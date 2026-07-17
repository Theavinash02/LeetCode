from collections import Counter
import itertools
import bisect

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_num = max(nums)
        
        # 1. Count frequencies of each number
        freq = Counter(nums)
        
        # 2. count_divisors[d] stores how many elements in nums are multiples of d
        count_divisors = [0] * (max_num + 1)
        for d in range(1, max_num + 1):
            for multiple in range(d, max_num + 1, d):
                count_divisors[d] += freq[multiple]
                
        # 3. count_gcd[g] stores the exact number of pairs with GCD equal to g
        count_gcd = [0] * (max_num + 1)
        for g in range(max_num, 0, -1):
            v = count_divisors[g]
            # Total possible pairs formed by multiples of g
            total_pairs = v * (v - 1) // 2
            
            # Subtract pairs that actually have a strictly larger GCD (2g, 3g, ...)
            for larger_g in range(2 * g, max_num + 1, g):
                total_pairs -= count_gcd[larger_g]
                
            count_gcd[g] = total_pairs
            
        # 4. Create prefix sums to represent the cumulative count of sorted GCD pairs
        prefix_sums = list(itertools.accumulate(count_gcd))
        
        # 5. Answer each query using binary search
        ans = []
        for q in queries:
            # Find the first index where prefix_sums[g] > q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans